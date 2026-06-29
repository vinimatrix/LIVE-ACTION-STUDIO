from celery import Celery
from app.core.config import settings
from app.agents.image_generator.image_generator import ImageGeneratorAgent

celery_app = Celery(
    "image_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

image_generator_agent = ImageGeneratorAgent()


@celery_app.task
def generate_image_from_prompt(image_data: dict):
    prompt = image_data.get("prompt")
    scene_id = image_data.get("scene_id")
    result = image_generator_agent.generate_image(prompt, scene_id)
    return result
