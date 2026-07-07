import os
import json
import base64
from fastapi import APIRouter, BackgroundTasks, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base as AppBase
from app.models import Job, Scene, Asset
from app.agents.director.director import DirectorAgent
from app.agents.storyboard.storyboard import StoryboardAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def _get_session():
    engine = create_engine("sqlite:///./manga_prompts.db", connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    AppBase.metadata.create_all(bind=engine)
    return SessionLocal()


@router.post("/process", status_code=202)
async def process_manga(manga_data: dict, background_tasks: BackgroundTasks):
    if not manga_data.get("filename"):
        raise HTTPException(status_code=400, detail="Filename is required")

    background_tasks.add_task(
        DirectorAgent().process_manga_request, manga_data
    )

    return {
        "message": "Processing started",
        "filename": manga_data.get("filename"),
        "status": "accepted"
    }


@router.post("/upload")
async def upload_manga(file: UploadFile = File(...), character_map: str = Form("{}"), manga: str = Form("")):
    ext = os.path.splitext(file.filename or "page.jpg")[1] or ".jpg"
    dest = os.path.join(UPLOAD_DIR, f"{os.urandom(4).hex()}{ext}")
    with open(dest, "wb") as f:
        content = await file.read()
        f.write(content)

    image_base64 = base64.b64encode(content).decode()
    char_map = json.loads(character_map)

    db = _get_session()
    try:
        director = DirectorAgent(db_session=lambda: db)
        job_id = director.process_manga_request({
            "filename": file.filename or "page.jpg",
            "manga": manga,
            "image": image_base64,
            "character_mapping": char_map,
            "options": {"max_scenes": 5},
        })

        job = db.query(Job).filter(Job.id == job_id).first()
        assets = (
            db.query(Asset)
            .filter(Asset.job_id == job_id, Asset.asset_type == "prompt")
            .order_by(Asset.id)
            .all()
        )
        scenes_db = db.query(Scene).filter(Scene.job_id == job_id).all()

        scene_prompts = [
            {"scene_number": a.generation_metadata.get("scene_number", 0), "prompt_text": a.generation_metadata.get("prompt", "")}
            for a in assets
        ]

        storyboard_agent = StoryboardAgent()
        prompt_builder = FlowPromptBuilderAgent()
        scenes_data = []
        for sc in scenes_db:
            meta = next((a.generation_metadata for a in assets if a.scene_id == sc.id), {})
            scenes_data.append({
                "scene_id": sc.id,
                "duration": sc.duration,
                "characters": meta.get("characters", []),
                "description": sc.description,
                "camera": meta.get("camera", {}),
                "lighting": meta.get("lighting", {}),
                "dialogue": meta.get("dialogue", []),
                "transition": "cut",
            })
        storyboard_result = prompt_builder.build_storyboard_prompts(
            scenes_data, char_map, storyboard_agent
        )
        storyboard_prompts = [
            {"scene_number": sp["scene_number"], "prompt_text": sp["prompt_text"], "shots": sp.get("shots", [])}
            for sp in storyboard_result
        ]

        return JSONResponse({
            "job_id": job.id,
            "filename": job.manga_filename,
            "status": job.status,
            "scene_prompts": scene_prompts,
            "storyboard_prompts": storyboard_prompts,
        })
    finally:
        db.close()
        os.remove(dest)


@router.get("/status/{job_id}")
async def get_job_status(job_id: int):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        return {
            "job_id": job.id,
            "status": job.status,
            "progress": job.progress,
            "current_step": job.current_step,
            "error_message": job.error_message
        }
    finally:
        db.close()


@router.get("/result/{job_id}")
async def get_job_result(job_id: int):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        if job.status != "completed":
            raise HTTPException(
                status_code=400,
                detail=f"Job is not completed yet (status: {job.status})"
            )

        assets = db.query(Asset).filter(Asset.job_id == job_id).all()
        video_asset = None
        for asset in assets:
            if asset.asset_type == "video" and "final" in (asset.file_path or ""):
                video_asset = asset
                break

        if not video_asset:
            raise HTTPException(status_code=404, detail="Result not found")

        return {
            "job_id": job.id,
            "video_url": f"/assets/{video_asset.file_path}",
            "assets": [
                {"id": asset.id, "type": asset.asset_type, "file_path": asset.file_path}
                for asset in assets
            ]
        }
    finally:
        db.close()
