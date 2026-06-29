from celery import Celery
from app.core.config import settings
from app.agents.voice_generator.voice_generator import VoiceGeneratorAgent

celery_app = Celery(
    "voice_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

voice_generator_agent = VoiceGeneratorAgent()


@celery_app.task
def generate_voice_from_prompt(voice_data: dict):
    prompt = voice_data.get("prompt")
    character_id = voice_data.get("character_id")
    result = voice_generator_agent.generate_voice(prompt, character_id)
    return result
