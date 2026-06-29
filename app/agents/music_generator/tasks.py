from celery import Celery
from app.core.config import settings
from app.agents.music_generator.music_generator import MusicGeneratorAgent

celery_app = Celery(
    "music_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

music_generator_agent = MusicGeneratorAgent()


@celery_app.task
def generate_music_from_prompt(music_data: dict):
    prompt = music_data.get("prompt")
    duration = music_data.get("duration", 5.0)
    result = music_generator_agent.generate_music(prompt, duration)
    return result
