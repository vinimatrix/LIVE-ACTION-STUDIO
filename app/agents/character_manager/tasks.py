from celery import Celery
from app.core.config import settings
from app.agents.character_manager.character_manager import CharacterManagerAgent

celery_app = Celery(
    "character_manager",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

character_manager_agent = CharacterManagerAgent()


@celery_app.task
def process_screenplay_characters(screenplay_data: dict):
    result = character_manager_agent.process_screenplay(screenplay_data)
    return result
