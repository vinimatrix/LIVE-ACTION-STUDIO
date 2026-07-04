from typing import Dict, Any, List

class SceneComposerAgent:
    def __init__(self):
        self.max_duration = 10.0

    def compose(self, manga_analysis: Dict[str, Any], max_scenes: int = 5) -> List[Dict[str, Any]]:
        characters = manga_analysis.get("characters", [])
        setting = manga_analysis.get("setting", "Unknown setting")
        action = manga_analysis.get("action", "")
        dialogue = manga_analysis.get("dialogue", [])
        mood = manga_analysis.get("mood", "neutral")

        scenes = []
        num_dialogues = len(dialogue)

        if num_dialogues <= 1 and not action:
            scenes.append(self._build_scene(1, characters, setting, action, dialogue, mood, "wide", "static"))
        else:
            for i in range(min(max_scenes, max(1, num_dialogues))):
                scene_dialogue = dialogue[i:i+1] if i < num_dialogues else []
                shot_type = self._select_shot(i, num_dialogues)
                movement = self._select_movement(i)
                desc = f"{action} - Part {i+1}" if num_dialogues > 1 else action
                scenes.append(self._build_scene(
                    i + 1, characters, setting, desc, scene_dialogue, mood, shot_type, movement
                ))

        return scenes

    def _build_scene(self, scene_id, characters, setting, action, dialogue, mood, shot_type, movement):
        return {
            "scene_id": scene_id,
            "duration": min(self.max_duration, 8.0 + len(dialogue) * 2),
            "characters": [
                {"name": c.get("name", "Unknown"), "appearance": c.get("appearance", ""),
                 "expression": c.get("expression", "neutral"), "position": c.get("position", "frame")}
                for c in characters
            ],
            "description": action,
            "camera": {"shot_type": shot_type, "movement": movement, "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset" if "sunset" in setting.lower() or "sun" in setting.lower() else "day",
                         "mood_lighting": mood},
            "dialogue": [{"character": d.split("!")[0] if "!" in d else "Character", "text": d} for d in dialogue],
            "transition": "cut" if scene_id > 1 else "fade_in"
        }

    def _select_shot(self, index, total):
        shots = ["wide", "medium", "close-up", "over-the-shoulder", "extreme-close-up"]
        return shots[index % len(shots)]

    def _select_movement(self, index):
        movements = ["static", "dolly", "pan", "tilt", "steadicam"]
        return movements[index % len(movements)]
