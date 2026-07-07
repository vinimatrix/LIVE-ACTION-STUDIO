from typing import Dict, Any, List

MOOD_SPEED = {
    "tenso": 0.7, "tension": 0.7, "accion": 0.7, "rapido": 0.7,
    "confrontacion": 0.7, "frustracion": 0.75, "discusion": 0.75,
    "neutral": 1.0,
    "melancolico": 1.3, "sereno": 1.3, "misterioso": 1.2,
    "epico": 1.2, "triste": 1.2, "sombrío": 1.1, "tristeza": 1.2,
    "suspenso": 0.9, "calma": 1.4, "pacífico": 1.3,
}

_KEYS = sorted(MOOD_SPEED, key=len, reverse=True)


def _normalize(s: str) -> str:
    trans = str.maketrans("áéíóúüñ", "aeiouun")
    return s.lower().translate(trans)


def _estimate_duration(dialogue: List[str], action: str, mood: str) -> float:
    base = 3.0
    dialogue_time = len(dialogue) * 2.5
    action_bonus = 2.0 if action else 0.0
    raw = base + dialogue_time + action_bonus
    mn = _normalize(mood)
    speed = 1.0
    for key in _KEYS:
        if key in mn:
            speed = MOOD_SPEED[key]
            break
    return max(3.0, min(10.0, raw * speed))


def _tokens_of(scene: Dict[str, Any]) -> int:
    return len(scene["description"]) + sum(
        len(d.get("text", "")) for d in scene.get("dialogue", [])
    )


class SceneComposerAgent:
    def __init__(self):
        self.max_duration = 10.0

    def compose(self, manga_analysis: Dict[str, Any], max_scenes: int = 5, director_style: str = None) -> List[Dict[str, Any]]:
        characters = manga_analysis.get("characters", [])
        setting = manga_analysis.get("setting", "Unknown setting")
        action = manga_analysis.get("action", "")
        dialogue = manga_analysis.get("dialogue", [])
        mood = manga_analysis.get("mood", "neutral")
        panels = manga_analysis.get("panels", [])

        if not dialogue and not action and not panels:
            sc = self._build_scene(1, characters, setting, action, [], mood, "wide", "static")
            sc["director_style"] = director_style
            return [sc]

        raw_scenes = []
        if panels and len(panels) > 1:
            for i, panel in enumerate(panels):
                desc = panel.get("description", action or f"Panel {i+1}")
                start = (i * len(dialogue)) // len(panels)
                end = ((i + 1) * len(dialogue)) // len(panels)
                panel_dialogue = dialogue[start:end]
                sc = self._build_scene(
                    i + 1, characters, setting, desc, panel_dialogue, mood,
                    self._select_shot(i, len(panels)),
                    self._select_movement(i),
                )
                sc["director_style"] = director_style
                raw_scenes.append(sc)
        elif dialogue:
            for i, line in enumerate(dialogue):
                speaker = line["character"] if isinstance(line, dict) else (
                    line.split("!")[0] if "!" in str(line) else "Character"
                )
                text = line.get("text", line) if isinstance(line, dict) else line
                desc = f"{action} - {speaker}" if action else f"{speaker} habla"
                sc = self._build_scene(
                    i + 1, characters, setting, desc,
                    [{"character": speaker, "text": text}],
                    mood,
                    self._select_shot(i, len(dialogue)),
                    self._select_movement(i),
                )
                sc["director_style"] = director_style
                raw_scenes.append(sc)
        else:
            sc = self._build_scene(
                1, characters, setting, action, [], mood, "wide", "static"
            )
            sc["director_style"] = director_style
            raw_scenes.append(sc)

        for sc in raw_scenes:
            sc["duration"] = _estimate_duration(
                [d.get("text", str(d)) for d in sc.get("dialogue", [])],
                sc.get("description", ""),
                mood,
            )

        merged = self._merge_scenes(raw_scenes, self.max_duration)
        for i, sc in enumerate(merged):
            sc["scene_id"] = i + 1
        return merged[:max_scenes]

    def _merge_scenes(self, scenes: List[Dict[str, Any]], max_total: float) -> List[Dict[str, Any]]:
        if not scenes:
            return []
        result = [dict(scenes[0])]
        for sc in scenes[1:]:
            if result[-1]["duration"] + sc["duration"] <= max_total:
                prev = result[-1]
                prev["duration"] = min(max_total, prev["duration"] + sc["duration"])
                prev["dialogue"].extend(sc["dialogue"])
                prev["description"] += " / " + sc["description"]
                if len(prev["description"]) > 800:
                    prev["description"] = prev["description"][:797] + "..."
            else:
                result.append(dict(sc))
        return result

    def _build_scene(self, scene_id, characters, setting, action, dialogue, mood, shot_type, movement):
        return {
            "scene_id": scene_id,
            "duration": 5.0,
            "characters": [
                {"name": c.get("name", "Unknown"), "appearance": c.get("appearance", ""),
                 "expression": c.get("expression", "neutral"), "position": c.get("position", "frame")}
                for c in characters
            ],
            "description": action,
            "camera": {"shot_type": shot_type, "movement": movement, "lens": "35mm f/2.8"},
            "lighting": {"time_of_day": "sunset" if "sunset" in setting.lower() or "sun" in setting.lower() else "day",
                         "mood_lighting": mood},
            "dialogue": [
                {"character": d.get("character", "Character"), "text": d.get("text", str(d))}
                if isinstance(d, dict)
                else {"character": d.split("!")[0] if "!" in d else "Character", "text": d}
                for d in (dialogue if isinstance(dialogue, list) else [])
            ],
            "transition": "cut" if scene_id > 1 else "fade_in"
        }

    def _select_shot(self, index, total):
        shots = ["wide", "medium", "close-up", "over-the-shoulder", "extreme-close-up",
                 "low_angle", "high_angle", "birds_eye", "point_of_view"]
        return shots[index % len(shots)]

    def _select_movement(self, index):
        movements = ["static", "dolly", "pan", "tilt", "steadicam", "handheld",
                     "360_orbit", "crane_up", "crane_down", "drone_sweep", "whip_pan"]
        return movements[index % len(movements)]
