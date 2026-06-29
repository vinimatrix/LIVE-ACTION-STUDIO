from typing import Dict, Any, Callable
from app.core.config import settings
from app.models import Job, Scene
from app.db.session import SessionLocal


class DirectorAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal

    def process_manga_request(self, manga_data: Dict[str, Any]) -> int:
        db = self._db_session()
        try:
            job = Job(
                manga_filename=manga_data.get("filename", "unknown"),
                status="pending",
                progress=0,
                current_step="initializing"
            )
            db.add(job)
            db.commit()
            db.refresh(job)

            scene = Scene(
                manga_page_reference=manga_data.get("page_url", ""),
                description="Scene from manga page",
                dialogue=[],
                actions=[],
                duration=5.0,
                shot_type="wide",
                camera_movement="static",
                environment_id=1,
                job_id=job.id
            )
            db.add(scene)
            db.commit()

            return job.id
        finally:
            db.close()

    def get_next_task(self, job_id: int) -> Dict[str, Any]:
        db = self._db_session()
        try:
            job = db.query(Job).filter(Job.id == job_id).first()
            if not job:
                return {}

            scene = db.query(Scene).filter(Scene.job_id == job_id).first()
            if not scene:
                return {}

            return {
                "job_id": job.id,
                "scene_id": scene.id,
                "task_type": "process_scene",
                "data": {
                    "scene_id": scene.id,
                    "description": scene.description,
                    "duration": scene.duration
                }
            }
        finally:
            db.close()
