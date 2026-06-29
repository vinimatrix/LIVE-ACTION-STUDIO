from typing import Dict, Any
from app.core.config import settings


class PromptBuilderAgent:
    def __init__(self):
        self.settings = settings

    def build_image_prompt(self, scene_data: Dict[str, Any]) -> str:
        description = scene_data.get("description", "")
        character_parts = []
        for char_name, char_data in scene_data.get("character_data", {}).items():
            traits = ", ".join(char_data.get("personality_traits", []))
            character_parts.append(f"{char_name} ({traits})")

        character_str = ", ".join(character_parts) if character_parts else "no specific characters"

        env_data = scene_data.get("environment_data", {})
        env_desc = (
            f"{env_data.get('location_type', 'unknown')} with "
            f"{env_data.get('lighting_conditions', {}).get('time_of_day', 'day')} lighting"
        )

        camera = scene_data.get("camera_notes", {})
        shot_type = camera.get("shot_type", "wide")
        movement = camera.get("movement", "static")

        prompt = (
            f"A cinematic scene: {description}. Featuring {character_str}. "
            f"Setting: {env_desc}. Shot type: {shot_type}, {movement}. "
            f"High detail, professional photography, 8k."
        )

        return prompt

    def build_video_prompt(self, image_prompt: str, duration: float) -> str:
        return (
            f"{image_prompt}, smooth motion over {duration} seconds, "
            f"cinematic video, professional film quality"
        )

    def build_voice_prompt(self, dialogue: Dict[str, Any]) -> str:
        text = dialogue.get("text", "")
        emotion = dialogue.get("emotion", "neutral")
        character = dialogue.get("character", "Speaker")

        return f"{character} speaking with {emotion} emotion: {text}"

    def build_music_prompt(self, scene_data: Dict[str, Any]) -> str:
        duration = scene_data.get("duration", 5.0)
        if duration > 10:
            style = "epic orchestral"
        elif duration > 5:
            style = "dramatic tension"
        else:
            style = "brief ambient"

        return f"{style} background music for {duration} seconds"

    def build_effects_prompt(self, scene_data: Dict[str, Any]) -> str:
        actions = scene_data.get("actions", [])
        if any("explosion" in a.lower() or "fire" in a.lower() for a in actions):
            return "explosion and fire effects, realistic particle system"
        elif any("magic" in a.lower() or "spell" in a.lower() for a in actions):
            return "magical particle effects, glowing runes"
        else:
            return "subtle environmental effects, wind, light particles"
