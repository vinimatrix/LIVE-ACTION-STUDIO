from typing import Dict, Any, List


class StoryboardAgent:
    MAX_SHOT_DURATION = 8.0
    MIN_SHOT_DURATION = 4.0

    # Shot type patterns by mood
    MOOD_SHOT_PATTERNS = {
        "tense": ["close-up", "extreme-close-up", "close-up"],
        "intense": ["wide", "medium", "close-up"],
        "epic": ["extreme-wide", "wide", "close-up"],
        "sad": ["wide", "close-up", "extreme-close-up"],
        "peaceful": ["extreme-wide", "wide", "medium"],
    }

    # Default patterns by scenario
    PATTERN_DIALOGUE_1 = ["medium", "close-up"]
    PATTERN_DIALOGUE_2 = ["wide", "over-the-shoulder", "over-the-shoulder", "close-up"]
    PATTERN_ACTION = ["wide", "tracking", "close-up"]
    PATTERN_SILENT = ["wide", "slow_push-in", "extreme-close-up"]

    def break_down_scene(self, scene: Dict[str, Any]) -> List[Dict[str, Any]]:
        duration = scene.get("duration", 8.0)
        characters = scene.get("characters", [])
        dialogue = scene.get("dialogue", [])
        mood = scene.get("lighting", {}).get("mood_lighting", "neutral")
        camera = scene.get("camera", {})
        description = scene.get("description", "")

        if duration <= 5.0:
            return [self._build_single_shot(scene, 0, duration, camera, "fade_in" if scene.get("transition") == "fade_in" else "cut", "cut")]

        if len(dialogue) >= 2 and len(set(d["character"] for d in dialogue)) >= 2:
            return self._build_dialogue_two(scene)
        elif len(dialogue) == 1:
            return self._build_dialogue_one(scene)
        elif self._is_action_scene(mood):
            return self._build_action(scene)
        else:
            return self._build_silent_mood(scene, mood)

    def _build_single_shot(self, scene, start_time, end_time, camera, trans_in, trans_out):
        return {
            "shot_number": 1,
            "start_time": start_time,
            "end_time": end_time,
            "shot_type": camera.get("shot_type", "wide"),
            "movement": camera.get("movement", "static"),
            "lens": camera.get("lens", "35mm f/2.8"),
            "description": scene.get("description", ""),
            "characters_in_frame": [c["name"] for c in scene.get("characters", [])],
            "focus": scene.get("description", ""),
            "transition_in": trans_in,
            "transition_out": trans_out
        }

    def _build_dialogue_one(self, scene):
        duration = scene["duration"]
        mid = duration / 2
        return [
            self._build_shot(scene, 1, "medium", "static", "35mm f/2.8",
                0.0, mid, scene.get("description", ""),
                [c["name"] for c in scene.get("characters", [])],
                "Establecer personaje en entorno",
                scene.get("transition", "cut"), "cut"),
            self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                mid, duration, f"Close-up de {scene['characters'][0]['name']}: {scene['characters'][0].get('expression', 'neutral')}",
                [scene['characters'][0]['name']],
                f"Expresión facial de {scene['characters'][0]['name']}",
                "cut", "cut")
        ]

    def _build_dialogue_two(self, scene):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        char_names = [c["name"] for c in characters]
        n_shots = max(2, min(4, int(duration / StoryboardAgent.MIN_SHOT_DURATION)))
        shot_duration = duration / n_shots
        shots = []

        if n_shots == 2:
            shots.append(self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                0.0, shot_duration, f"Ambos personajes en cuadro: {', '.join(char_names)}",
                char_names, "Relación espacial entre personajes",
                scene.get("transition", "cut"), "cut"))
            shots.append(self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                shot_duration, duration, f"Clímax: {char_names[0]} confronta a {char_names[1]}",
                [char_names[0]], "Momento culminante del diálogo",
                "cut", "cut"))
        else:
            shots.append(self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                0.0, shot_duration, f"Ambos personajes en cuadro: {', '.join(char_names)}",
                char_names, "Relación espacial entre personajes",
                scene.get("transition", "cut"), "cut"))
            shots.append(self._build_shot(scene, 2, "over-the-shoulder", "static", "35mm f/2.8",
                shot_duration, shot_duration * 2, f"Sobre el hombro de {char_names[0]}: {char_names[1]} reacciona",
                [char_names[0], char_names[1]], f"Reacción de {char_names[1]}",
                "cut", "cut"))
            if n_shots >= 3:
                shots.append(self._build_shot(scene, 3, "over-the-shoulder", "static", "35mm f/2.8",
                    shot_duration * 2, shot_duration * 3, f"Sobre el hombro de {char_names[1]}: {char_names[0]} responde",
                    [char_names[0], char_names[1]], f"Respuesta de {char_names[0]}",
                    "cut", "cut"))
            if n_shots >= 4:
                shots.append(self._build_shot(scene, 4, "close-up", "slow push-in", "50mm f/2.0",
                    shot_duration * 3, duration, f"Clímax: {char_names[0]} confronta a {char_names[1]}",
                    [char_names[0]], "Momento culminante del diálogo",
                    "cut", "cut"))

        return shots

    def _build_action(self, scene):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        n_shots = 3
        shot_duration = duration / n_shots
        return [
            self._build_shot(scene, 1, "wide", "tracking", "24mm f/4",
                0.0, shot_duration, scene.get("description", ""),
                [c["name"] for c in characters], "Contexto de la acción",
                scene.get("transition", "cut"), "cut"),
            self._build_shot(scene, 2, "medium", "tracking", "35mm f/2.8",
                shot_duration, shot_duration * 2, f"Movimiento de {characters[0]['name'] if characters else 'personaje'} en acción",
                [c["name"] for c in characters], "Seguimiento del movimiento",
                "cut", "cut"),
            self._build_shot(scene, 3, "close-up", "static", "50mm f/2.0",
                shot_duration * 2, duration, "Impacto o efecto de la acción",
                [c["name"] for c in characters], "Momento de impacto",
                "cut", "cut")
        ]

    def _build_silent_mood(self, scene, mood):
        duration = scene["duration"]
        characters = scene.get("characters", [])
        pattern = self.MOOD_SHOT_PATTERNS.get(mood, self.PATTERN_SILENT)
        n_shots = min(len(pattern), max(2, int(duration / 5)))
        shot_duration = duration / n_shots
        shots = []
        for i in range(n_shots):
            shot_type = pattern[i] if i < len(pattern) else "medium"
            movement = "static" if shot_type in ("close-up", "extreme-close-up") else "slow dolly"
            if i == n_shots - 1:
                lens = "85mm f/1.4" if shot_type == "extreme-close-up" else "50mm f/2.0"
            else:
                lens = "24mm f/4" if shot_type in ("wide", "extreme-wide") else "35mm f/2.8"
            shots.append(self._build_shot(scene, i + 1, shot_type, movement, lens,
                i * shot_duration, (i + 1) * shot_duration,
                f"{shot_type.replace('_', ' ').title()} — construyendo atmósfera ({mood})",
                [c["name"] for c in characters] if i == 0 else [],
                f"Enfoque en {shot_type}: atmósfera {mood}",
                "cut" if i > 0 else scene.get("transition", "cut"), "cut"))
        return shots

    def _build_shot(self, scene, shot_number, shot_type, movement, lens,
                    start_time, end_time, description, characters_in_frame,
                    focus, transition_in, transition_out):
        return {
            "shot_number": shot_number,
            "start_time": start_time,
            "end_time": end_time,
            "shot_type": shot_type,
            "movement": movement,
            "lens": lens,
            "description": description,
            "characters_in_frame": characters_in_frame,
            "focus": focus,
            "transition_in": transition_in,
            "transition_out": transition_out
        }

    def _is_action_scene(self, mood: str) -> bool:
        return mood in ("intense", "epic", "dramatic", "explosive")
