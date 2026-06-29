from celery import Celery
from app.core.config import settings
from app.agents.screenwriter.screenwriter import ScreenwriterAgent

celery_app = Celery(
    "screenwriter",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

screenwriter_agent = ScreenwriterAgent()


@celery_app.task
def process_scene_screenplay(screenplay_data: dict):
    result = screenwriter_agent.process_scene(screenplay_data)
    return result
