from typing import Dict, Any
from app.core.config import settings
import re
import logging

logger = logging.getLogger(__name__)


class ScreenwriterAgent:
    def __init__(self):
        self.settings = settings

    def adapt_to_latin_spanish(self, text: str) -> str:
        """
        Convert Spanish from Spain to neutral Latin American Spanish.

        Args:
            text: Input text in Spanish

        Returns:
            Adapted text in neutral Latin American Spanish

        Raises:
            TypeError: If input is not a string
        """
        if not isinstance(text, str):
            logger.error(f"Expected string input, got {type(text)}")
            raise TypeError(f"Input must be a string, got {type(text)}")

        if not text:
            return text

        try:
            # Replacements for vosotros forms to ustedes
            replacements = [
                (r"\b[Vv]osotros\b", lambda m: "Ustedes" if m.group(0).istitle() else "ustedes"),
                (r"\b[Vv]osotras\b", lambda m: "Ustedes" if m.group(0).istitle() else "ustedes"),
                (r"\b[Oo]s lo\b", lambda m: "Se lo" if m.group(0).istitle() else "se lo"),
                (r"\b[Oo]s la\b", lambda m: "Se la" if m.group(0).istitle() else "se la"),
                (r"\b[Oo]s los\b", lambda m: "Se los" if m.group(0).istitle() else "se los"),
                (r"\b[Oo]s las\b", lambda m: "Se las" if m.group(0).istitle() else "se las"),
                (r"\b[Oo]s\b", lambda m: "Les" if m.group(0).istitle() else "les"),
                (r"\b[Vv]uestro\b", lambda m: "Su" if m.group(0).istitle() else "su"),
                (r"\b[Vv]uestra\b", lambda m: "Su" if m.group(0).istitle() else "su"),
                (r"\b[Vv]uestros\b", lambda m: "Sus" if m.group(0).istitle() else "sus"),
                (r"\b[Vv]uestras\b", lambda m: "Sus" if m.group(0).istitle() else "sus"),

                # Verbos en segunda persona del plural y imperativos
                (r"\b[Ee]ntendéis\b", lambda m: "Entienden" if m.group(0).istitle() else "entienden"),
                (r"\b[Ee]xplicáis\b", lambda m: "Explican" if m.group(0).istitle() else "explican"),
                (r"\b[Hh]acéis\b", lambda m: "Hacen" if m.group(0).istitle() else "hacen"),
                (r"\b[Tt]enéis\b", lambda m: "Tienen" if m.group(0).istitle() else "tienen"),
                (r"\b[Pp]odéis\b", lambda m: "Pueden" if m.group(0).istitle() else "pueden"),
                (r"\b[Qq]ueréis\b", lambda m: "Quieren" if m.group(0).istitle() else "quieren"),
                (r"\b[Vv]ais\b", lambda m: "Van" if m.group(0).istitle() else "van"),
                (r"\b[Ss]ois\b", lambda m: "Son" if m.group(0).istitle() else "son"),
                (r"\b[Ee]stáis\b", lambda m: "Están" if m.group(0).istitle() else "están"),
                (r"\b[Ss]abéis\b", lambda m: "Saben" if m.group(0).istitle() else "saben"),
                (r"\b[Dd]ecís\b", lambda m: "Dicen" if m.group(0).istitle() else "dicen"),
                (r"\b[Vv]enís\b", lambda m: "Vienen" if m.group(0).istitle() else "vienen"),
                (r"\b[Vv]eréis\b", lambda m: "Verán" if m.group(0).istitle() else "verán"),
                (r"\b[Ii]réis\b", lambda m: "Irán" if m.group(0).istitle() else "irán"),
                (r"\b[Hh]aréis\b", lambda m: "Harán" if m.group(0).istitle() else "harán"),

                (r"\b[Ee]ntended\b", lambda m: "Entiendan" if m.group(0).istitle() else "entiendan"),
                (r"\b[Dd]ejad\b", lambda m: "Dejen" if m.group(0).istitle() else "dejen"),
                (r"\b[Mm]irad\b", lambda m: "Miren" if m.group(0).istitle() else "miren"),
                (r"\b[Ee]scuchad\b", lambda m: "Escuchen" if m.group(0).istitle() else "escuchen"),
                (r"\b[Ii]d\b", lambda m: "Vayan" if m.group(0).istitle() else "vayan"),
                (r"\b[Hh]aced\b", lambda m: "Hagan" if m.group(0).istitle() else "hagan"),
                (r"\b[Dd]ecid\b", lambda m: "Digan" if m.group(0).istitle() else "digan"),
                (r"\b[Vv]olved\b", lambda m: "Vuelvan" if m.group(0).istitle() else "vuelvan"),
                (r"\b[Tt]raed\b", lambda m: "Traigan" if m.group(0).istitle() else "traigan"),
                (r"\b[Pp]oned\b", lambda m: "Pongan" if m.group(0).istitle() else "pongan"),
                (r"\b[Ss]alid\b", lambda m: "Salgan" if m.group(0).istitle() else "salgan"),
                (r"\b[Vv]enid\b", lambda m: "Vengan" if m.group(0).istitle() else "vengan"),

                # Modismos comunes
                (r"\b[Ll]a caradura\b", lambda m: "El descaro" if m.group(0).istitle() else "el descaro"),
                (r"\b[Ee]l caradura\b", lambda m: "El descarado" if m.group(0).istitle() else "el descarado"),
                (r"\b[Cc]aradura\b", lambda m: "Descarado" if m.group(0).istitle() else "descarado"),
                (r"\b[Gg]ilipollas\b", lambda m: "Imbécil" if m.group(0).istitle() else "imbécil"),
                (r"\b[Tt]ío\b", lambda m: "Oye" if m.group(0).istitle() else "oye"),
                (r"\b[Tt]ia\b", lambda m: "Oye" if m.group(0).istitle() else "oye"),
                (r"\b[Oo]rdenador\b", lambda m: "Computadora" if m.group(0).istitle() else "computadora"),
                (r"\b[Mm]óvil\b", lambda m: "Celular" if m.group(0).istitle() else "celular"),
                (r"\b[Pp]atata\b", lambda m: "Papa" if m.group(0).istitle() else "papa"),
                (r"\b[Cc]oche\b", lambda m: "Carro" if m.group(0).istitle() else "carro"),
            ]

            result = text
            for pattern, repl in replacements:
                result = re.sub(pattern, repl, result)

            return result
        except Exception as e:
            logger.exception(f"Error adapting text to Latin Spanish: {e}")
            # Return original text as fallback
            return text

    def process_scene(self, scene_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a scene dictionary into a screenplay format.

        Args:
            scene_data: Dictionary containing scene information

        Returns:
            Dictionary with screenplay elements

        Raises:
            TypeError: If scene_data is not a dictionary
            KeyError: If required fields are missing
        """
        if not isinstance(scene_data, dict):
            logger.error(f"Expected dict for scene_data, got {type(scene_data)}")
            raise TypeError(f"scene_data must be a dictionary, got {type(scene_data)}")

        try:
            scene_id = scene_data.get("scene_id")
            description = scene_data.get("description", "")
            duration = scene_data.get("duration", 5.0)
            dialogues_in = scene_data.get("dialogue", [])

            if not dialogues_in:
                dialogue = [
                    {
                        "character": "Narrator",
                        "text": f"This scene describes {description}",
                        "emotion": "neutral"
                    }
                ]
            else:
                dialogue = []
                for d in dialogues_in:
                    if not isinstance(d, dict):
                        logger.warning(f"Skipping invalid dialogue entry: {d}")
                        continue

                    text_adapted = self.adapt_to_latin_spanish(d.get("text", ""))
                    dialogue.append({
                        "character": d.get("character", "Speaker"),
                        "text": text_adapted,
                        "emotion": d.get("emotion", "neutral")
                    })

            actions = scene_data.get("actions", [])
            if not actions:
                actions = [
                    f"Show the scene: {description}",
                    f"Hold for {duration} seconds"
                ]

            screenplay = {
                "scene_id": scene_id,
                "description": description,
                "dialogue": dialogue,
                "actions": actions,
                "camera_notes": {
                    "shot_type": "wide",
                    "movement": "static",
                    "focus": "deep"
                },
                "duration": duration
            }

            return screenplay
        except Exception as e:
            logger.exception(f"Error processing scene {scene_data.get('scene_id', 'unknown')}: {e}")
            raise