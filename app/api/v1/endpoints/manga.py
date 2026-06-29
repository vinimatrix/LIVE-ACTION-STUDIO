from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.db.session import SessionLocal
from app.models import Job, Asset
from app.agents.director.director import DirectorAgent

router = APIRouter()


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
