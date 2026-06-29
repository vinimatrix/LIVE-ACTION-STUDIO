from fastapi import APIRouter, HTTPException
from app.db.session import SessionLocal
from app.models import Job

router = APIRouter()


@router.get("/")
async def list_jobs(limit: int = 10, offset: int = 0):
    db = SessionLocal()
    try:
        jobs = (
            db.query(Job)
            .order_by(Job.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
        return [
            {
                "id": job.id,
                "filename": job.manga_filename,
                "status": job.status,
                "progress": job.progress,
                "created_at": job.created_at.isoformat() if job.created_at else None,
            }
            for job in jobs
        ]
    finally:
        db.close()


@router.get("/{job_id}")
async def get_job(job_id: int):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        return {
            "id": job.id,
            "filename": job.manga_filename,
            "status": job.status,
            "progress": job.progress,
            "current_step": job.current_step,
            "error_message": job.error_message,
            "created_at": job.created_at.isoformat() if job.created_at else None,
            "updated_at": job.updated_at.isoformat() if job.updated_at else None,
        }
    finally:
        db.close()
