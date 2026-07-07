from typing import Dict, Any, Callable
from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Job, Scene, Asset
from app.models.asset import AssetType
from app.agents.manga_analyzer.manga_analyzer import MangaAnalyzerAgent
from app.agents.scene_composer.scene_composer import SceneComposerAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent


class DirectorAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal
        self.manga_analyzer = MangaAnalyzerAgent()
        self.scene_composer = SceneComposerAgent()
        self.prompt_builder = FlowPromptBuilderAgent()

    def process_manga_request(self, manga_data: Dict[str, Any]) -> int:
        image = manga_data.get("image", "")
        filename = manga_data.get("filename", "")
        manga_series = manga_data.get("manga", "")
        character_mapping = manga_data.get("character_mapping", {})
        options = manga_data.get("options", {})
        max_scenes = options.get("max_scenes", 5)

        analysis = self.manga_analyzer.analyze(image, filename, manga_series)
        scenes = self.scene_composer.compose(analysis, max_scenes)
        prompts = self.prompt_builder.build_prompts(scenes, character_mapping)

        db = self._db_session()
        try:
            job = Job(
                manga_filename=filename,
                status="completed",
                progress=100,
                current_step="prompts_generated"
            )
            db.add(job)
            db.flush()

            for scene_data, prompt in zip(scenes, prompts):
                scene = Scene(
                    job_id=job.id,
                    manga_page_reference=filename,
                    description=scene_data.get("description", ""),
                    duration=scene_data.get("duration", 8.0)
                )
                db.add(scene)
                db.flush()

                asset = Asset(
                    job_id=job.id,
                    scene_id=scene.id,
                    asset_type=AssetType.PROMPT,
                    file_path="",
                    mime_type="text/markdown",
                    generation_metadata={
                        "prompt": prompt["prompt_text"],
                        "scene_number": prompt["scene_number"],
                        "duration": prompt["duration"],
                        "manga_analysis": analysis,
                        "characters": scene_data.get("characters", []),
                        "camera": scene_data.get("camera", {}),
                        "lighting": scene_data.get("lighting", {}),
                        "dialogue": scene_data.get("dialogue", []),
                    }
                )
                db.add(asset)

            db.commit()
            db.refresh(job)
            return job.id
        finally:
            db.close()

    def get_next_task(self, job_id: int) -> Dict[str, Any]:
        db = self._db_session()
        try:
            job = db.query(Job).filter(Job.id == job_id).first()
            if not job:
                return {"error": "Job not found"}
            return {"job_id": job.id, "task_type": "completed", "status": job.status}
        finally:
            db.close()
