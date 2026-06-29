from celery import Celery
from app.core.config import settings
from app.agents.video_generator.video_generator import VideoGeneratorAgent

celery_app = Celery(
    "video_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

video_generator_agent = VideoGeneratorAgent()


@celery_app.task
def generate_video_from_image(video_data: dict):
    image_path = video_data.get("image_path")
    prompt = video_data.get("prompt")
    duration = video_data.get("duration", 5.0)
    result = video_generator_agent.generate_video(image_path, prompt, duration)
    return result
