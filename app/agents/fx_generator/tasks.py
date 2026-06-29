from celery import Celery
from app.core.config import settings
from app.agents.fx_generator.fx_generator import FXGeneratorAgent

celery_app = Celery(
    "fx_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

fx_generator_agent = FXGeneratorAgent()


@celery_app.task
def generate_fx_from_prompt(fx_data: dict):
    prompt = fx_data.get("prompt")
    duration = fx_data.get("duration", 5.0)
    result = fx_generator_agent.generate_effect(prompt, duration)
    return result
