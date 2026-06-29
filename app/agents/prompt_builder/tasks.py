from celery import Celery
from app.core.config import settings
from app.agents.prompt_builder.prompt_builder import PromptBuilderAgent

celery_app = Celery(
    "prompt_builder",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

prompt_builder_agent = PromptBuilderAgent()


@celery_app.task
def build_prompts(screenplay_data: dict):
    image_prompt = prompt_builder_agent.build_image_prompt(screenplay_data)
    video_prompt = prompt_builder_agent.build_video_prompt(
        image_prompt,
        screenplay_data.get("duration", 5.0)
    )

    voice_prompts = []
    for dialogue in screenplay_data.get("dialogue", []):
        voice_prompts.append(prompt_builder_agent.build_voice_prompt(dialogue))

    music_prompt = prompt_builder_agent.build_music_prompt(screenplay_data)
    effects_prompt = prompt_builder_agent.build_effects_prompt(screenplay_data)

    return {
        "image_prompt": image_prompt,
        "video_prompt": video_prompt,
        "voice_prompts": voice_prompts,
        "music_prompt": music_prompt,
        "effects_prompt": effects_prompt
    }
