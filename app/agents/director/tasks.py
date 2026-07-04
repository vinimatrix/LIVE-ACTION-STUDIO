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
def process_manga_pipeline(manga_data: dict):
    job_id = director_agent.process_manga_request(manga_data)
    return job_id
