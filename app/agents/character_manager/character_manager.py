from typing import Dict, Any, Callable
from app.core.config import settings
from app.models import Character
from app.db.session import SessionLocal


class CharacterManagerAgent:
    def __init__(self, db_session: Callable = None):
        self.settings = settings
        self._db_session = db_session or SessionLocal

    def get_or_create_character(self, character_name: str, traits: list = None) -> Dict[str, Any]:
        db = self._db_session()
        try:
            character = db.query(Character).filter(
                Character.name == character_name
            ).first()

            if character:
                if traits:
                    character.personality_traits = traits
                db.commit()
                db.refresh(character)
            else:
                character = Character(
                    name=character_name,
                    description=f"Character {character_name}",
                    visual_references=[],
                    personality_traits=traits or ["neutral"],
                    expressions=["neutral"],
                    outfits=[],
                    weapons=[],
                    abilities=[],
                    voice_profile="default_voice"
                )
                db.add(character)
                db.commit()
                db.refresh(character)

            return {
                "id": character.id,
                "name": character.name,
                "visual_references": character.visual_references,
                "personality_traits": character.personality_traits,
                "expressions": character.expressions,
                "outfits": character.outfits,
                "weapons": character.weapons,
                "abilities": character.abilities,
                "voice_profile": character.voice_profile
            }
        finally:
            db.close()

    def process_screenplay(self, screenplay_data: Dict[str, Any]) -> Dict[str, Any]:
        character_names = set()
        for dialogue in screenplay_data.get("dialogue", []):
            char_name = dialogue.get("character", "Narrator")
            if char_name != "Narrator":
                character_names.add(char_name)

        character_data = {}
        for name in character_names:
            character_data[name] = self.get_or_create_character(name, [])

        enhanced = screenplay_data.copy()
        enhanced["character_data"] = character_data

        return enhanced
