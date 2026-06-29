from celery import Celery
from app.core.config import settings
from app.agents.environment_manager.environment_manager import EnvironmentManagerAgent

celery_app = Celery(
    "environment_manager",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

environment_manager_agent = EnvironmentManagerAgent()


@celery_app.task
def process_screenplay_environment(screenplay_data: dict):
    result = environment_manager_agent.process_screenplay(screenplay_data)
    return result
