from celery import Celery
from app.core.config import settings
from app.agents.director.director import DirectorAgent

celery_app = Celery(
    "director",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

director_agent = DirectorAgent()


@celery_app.task
def process_manga_page(manga_data: dict):
    job_id = director_agent.process_manga_request(manga_data)
    process_scene.delay({"job_id": job_id})
    return job_id


@celery_app.task
def process_scene(task_data: dict):
    job_id = task_data.get("job_id")
    from app.db.session import SessionLocal
    from app.models import Job
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if job:
            job.progress = 50
            job.current_step = "scene_processed"
            db.commit()
    finally:
        db.close()

    return {"status": "scene_processed", "job_id": job_id}
