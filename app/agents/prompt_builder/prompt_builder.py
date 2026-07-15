from typing import Dict, Any
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class PromptBuilderAgent:
    def __init__(self):
        self.settings = settings

    def build_image_prompt(self, scene_data: Dict[str, Any]) -> str:
        """
        Build an image generation prompt from scene data.

        Args:
            scene_data: Dictionary containing scene information

        Returns:
            Formatted prompt string for image generation

        Raises:
            TypeError: If scene_data is not a dictionary
        """
        if not isinstance(scene_data, dict):
            logger.error(f"Expected dict for scene_data, got {type(scene_data)}")
            raise TypeError(f"scene_data must be a dictionary, got {type(scene_data)}")

        try:
            description = scene_data.get("description", "")
            character_parts = []
            for char_name, char_data in scene_data.get("character_data", {}).items():
                if not isinstance(char_data, dict):
                    logger.warning(f"Skipping invalid character data for {char_name}: {char_data}")
                    continue

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
                f"A photorealistic live-action cinematic scene: {description}. Featuring {character_str}. "
                f"Setting: {env_desc}. Shot type: {shot_type}, {movement}. "
                f"Ultra realistic, 8k resolution, highly detailed skin textures, volumetric lighting, "
                f"shot on 35mm lens, professional cinematography, movie-like quality, no CGI, no 3D render. "
                f"Strictly maintain consistency with the characters and location without hallucinating extra details."
            )

            return prompt
        except Exception as e:
            logger.exception(f"Error building image prompt: {e}")
            # Return a basic prompt as fallback
            return f"A cinematic scene: {scene_data.get('description', 'unknown scene')}"

    def build_video_prompt(self, image_prompt: str, duration: float) -> str:
        """
        Build a video generation prompt from an image prompt and duration.

        Args:
            image_prompt: Base image prompt
            duration: Duration in seconds

        Returns:
            Formatted prompt string for video generation

        Raises:
            TypeError: If image_prompt is not a string or duration is not a number
            ValueError: If duration is negative
        """
        if not isinstance(image_prompt, str):
            logger.error(f"Expected string for image_prompt, got {type(image_prompt)}")
            raise TypeError(f"image_prompt must be a string, got {type(image_prompt)}")

        if not isinstance(duration, (int, float)):
            logger.error(f"Expected numeric duration, got {type(duration)}")
            raise TypeError(f"duration must be a number, got {type(duration)}")

        if duration < 0:
            logger.error(f"Duration cannot be negative: {duration}")
            raise ValueError("duration must be non-negative")

        try:
            return (
                f"{image_prompt}, smooth realistic motion over {duration} seconds, "
                f"live-action cinematic video, photorealistic professional film quality"
            )
        except Exception as e:
            logger.exception(f"Error building video prompt: {e}")
            # Return a basic prompt as fallback
            return f"{image_prompt}, motion over {duration} seconds"

    def build_voice_prompt(self, dialogue: Dict[str, Any]) -> str:
        """
        Build a voice generation prompt from dialogue data.

        Args:
            dialogue: Dictionary containing dialogue information

        Returns:
            Formatted prompt string for voice generation

        Raises:
            TypeError: If dialogue is not a dictionary
        """
        if not isinstance(dialogue, dict):
            logger.error(f"Expected dict for dialogue, got {type(dialogue)}")
            raise TypeError(f"dialogue must be a dictionary, got {type(dialogue)}")

        try:
            text = dialogue.get("text", "")
            emotion = dialogue.get("emotion", "neutral")
            character = dialogue.get("character", "Speaker")

            return f"{character} speaking with {emotion} emotion: {text}"
        except Exception as e:
            logger.exception(f"Error building voice prompt: {e}")
            # Return a basic prompt as fallback
            character = dialogue.get("character", "Speaker") if isinstance(dialogue, dict) else "Speaker"
            text = dialogue.get("text", "") if isinstance(dialogue, dict) else str(dialogue)
            return f"{character} speaking: {text}"

    def build_music_prompt(self, scene_data: Dict[str, Any]) -> str:
        """
        Build a music generation prompt from scene data.

        Args:
            scene_data: Dictionary containing scene information

        Returns:
            Formatted prompt string for music generation

        Raises:
            TypeError: If scene_data is not a dictionary
        """
        if not isinstance(scene_data, dict):
            logger.error(f"Expected dict for scene_data, got {type(scene_data)}")
            raise TypeError(f"scene_data must be a dictionary, got {type(scene_data)}")

        try:
            duration = scene_data.get("duration", 5.0)
            if not isinstance(duration, (int, float)):
                logger.warning(f"Invalid duration type: {type(duration)}, using default 5.0")
                duration = 5.0

            if duration > 10:
                style = "epic orchestral"
            elif duration > 5:
                style = "dramatic tension"
            else:
                style = "brief ambient"

            return f"{style} background music for {duration} seconds"
        except Exception as e:
            logger.exception(f"Error building music prompt: {e}")
            # Return a basic prompt as fallback
            return f"background music for {scene_data.get('duration', 5)} seconds"

    def build_effects_prompt(self, scene_data: Dict[str, Any]) -> str:
        """
        Build an effects generation prompt from scene data.

        Args:
            scene_data: Dictionary containing scene information

        Returns:
            Formatted prompt string for effects generation

        Raises:
            TypeError: If scene_data is not a dictionary
        """
        if not isinstance(scene_data, dict):
            logger.error(f"Expected dict for scene_data, got {type(scene_data)}")
            raise TypeError(f"scene_data must be a dictionary, got {type(scene_data)}")

        try:
            actions = scene_data.get("actions", [])
            if not isinstance(actions, list):
                logger.warning(f"Actions is not a list: {type(actions)}, treating as empty")
                actions = []

            if any("explosion" in str(a).lower() or "fire" in str(a).lower() for a in actions):
                return "explosion and fire effects, realistic particle system"
            elif any("magic" in str(a).lower() or "spell" in str(a).lower() for a in actions):
                return "magical particle effects, glowing runes"
            else:
                return "subtle environmental effects, wind, light particles"
        except Exception as e:
            logger.exception(f"Error building effects prompt: {e}")
            # Return a safe fallback
            return "subtle environmental effects"