from typing import Dict, Any, List, Optional
from app.agents.director_styles import DIRECTOR_STYLES, resolve_style
import logging

logger = logging.getLogger(__name__)


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

    def break_down_scene(self, scene: Dict[str, Any], director_style: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Break down a scene into individual shots for storyboard creation.

        Args:
            scene: Dictionary containing scene information
            director_style: Optional director style to apply

        Returns:
            List of shot dictionaries

        Raises:
            TypeError: If scene is not a dictionary
        """
        if not isinstance(scene, dict):
            logger.error(f"Expected dict for scene, got {type(scene)}")
            raise TypeError(f"scene must be a dictionary, got {type(scene)}")

        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                logger.warning(f"Invalid duration for scene {scene.get('scene_id', 'unknown')}: {duration}, using default 8.0")
                duration = 8.0

            characters = scene.get("characters", [])
            if not isinstance(characters, list):
                logger.warning(f"Characters is not a list: {type(characters)}, treating as empty")
                characters = []

            dialogue = scene.get("dialogue", [])
            if not isinstance(dialogue, list):
                logger.warning(f"Dialogue is not a list: {type(dialogue)}, treating as empty")
                dialogue = []

            mood = scene.get("lighting", {}).get("mood_lighting", "neutral")
            camera = scene.get("camera", {})
            description = scene.get("description", "")

            if duration <= 5.0:
                return [self._build_single_shot(scene, 0, duration, camera, "fade_in" if scene.get("transition") == "fade_in" else "cut", "cut")]

            style = resolve_style(director_style, mood)
            config = DIRECTOR_STYLES.get(style)

            if config and self._is_action_scene(mood):
                return self._build_action_styled(scene, config, style)

            if len(dialogue) >= 2 and len(set(d.get("character", "") for d in dialogue if isinstance(d, dict))) >= 2:
                return self._build_dialogue_two(scene)
            elif len(dialogue) == 1:
                return self._build_dialogue_one(scene)
            elif self._is_action_scene(mood):
                return self._build_action(scene)
            else:
                return self._build_silent_mood(scene, mood)
        except Exception as e:
            logger.exception(f"Error breaking down scene {scene.get('scene_id', 'unknown')}: {e}")
            # Return a single shot as fallback
            camera = scene.get("camera", {}) if isinstance(scene.get("camera"), dict) else {}
            return [self._build_single_shot(scene, 0, scene.get("duration", 8.0) if isinstance(scene.get("duration"), (int, float)) and scene.get("duration") > 0 else 8.0, camera, "cut", "cut")]

    def _build_single_shot(self, scene, start_time, end_time, camera, trans_in, trans_out):
        """
        Build a single shot covering the entire scene.

        Args:
            scene: Scene dictionary
            start_time: Start time in seconds
            end_time: End time in seconds
            camera: Camera settings dictionary
            trans_in: Transition in type
            trans_out: Transition out type

        Returns:
            Shot dictionary
        """
        try:
            if not isinstance(camera, dict):
                logger.warning(f"Camera is not a dict: {type(camera)}, using empty dict")
                camera = {}

            return {
                "shot_number": 1,
                "start_time": float(start_time),
                "end_time": float(end_time),
                "shot_type": camera.get("shot_type", "wide"),
                "movement": camera.get("movement", "static"),
                "lens": camera.get("lens", "35mm f/2.8"),
                "description": scene.get("description", ""),
                "characters_in_frame": [c.get("name", "Unknown") for c in scene.get("characters", []) if isinstance(c, dict)],
                "focus": scene.get("description", ""),
                "transition_in": trans_in,
                "transition_out": trans_out,
                "slow_motion": False,
                "lens_flare": False,
                "dutch_angle": 0,
                "director_style": None,
            }
        except Exception as e:
            logger.exception(f"Error building single shot: {e}")
            # Return a minimal valid shot
            return {
                "shot_number": 1,
                "start_time": float(start_time) if isinstance(start_time, (int, float)) else 0.0,
                "end_time": float(end_time) if isinstance(end_time, (int, float)) else 8.0,
                "shot_type": "wide",
                "movement": "static",
                "lens": "35mm f/2.8",
                "description": scene.get("description", "") if isinstance(scene.get("description"), str) else "",
                "characters_in_frame": [],
                "focus": "",
                "transition_in": "cut",
                "transition_out": "cut",
                "slow_motion": False,
                "lens_flare": False,
                "dutch_angle": 0,
                "director_style": None,
            }

    def _build_dialogue_one(self, scene):
        """
        Build shots for a scene with single character dialogue.

        Args:
            scene: Scene dictionary

        Returns:
            List of two shot dictionaries
        """
        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                duration = 8.0

            mid = duration / 2
            return [
                self._build_shot(scene, 1, "medium", "static", "35mm f/2.8",
                                0.0, mid, scene.get("description", ""),
                                [c.get("name", "Unknown") for c in scene.get("characters", []) if isinstance(c, dict)],
                                "Establecer personaje en entorno",
                                scene.get("transition", "cut"), "cut"),
                self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                                mid, duration, f"Close-up de {scene['characters'][0].get('name', 'Character') if scene.get('characters') and isinstance(scene['characters'], list) and len(scene['characters']) > 0 and isinstance(scene['characters'][0], dict) else 'Character'}: {scene['characters'][0].get('expression', 'neutral') if scene.get('characters') and isinstance(scene['characters'], list) and len(scene['characters']) > 0 and isinstance(scene['characters'][0], dict) else 'neutral'}",
                                [scene['characters'][0].get('name', 'Character') if scene.get('characters') and isinstance(scene['characters'], list) and len(scene['characters']) > 0 and isinstance(scene['characters'][0], dict) else 'Character'],
                                f"Expresión facial de {scene['characters'][0].get('name', 'Character') if scene.get('characters') and isinstance(scene['characters'], list) and len(scene['characters']) > 0 and isinstance(scene['characters'][0], dict) else 'Character'}",
                                "cut", "cut")
            ]
        except Exception as e:
            logger.exception(f"Error building dialogue one shots: {e}")
            # Return fallback shots
            duration = scene.get("duration", 8.0) if isinstance(scene.get("duration"), (int, float)) and scene.get("duration") > 0 else 8.0
            mid = duration / 2
            return [
                self._build_shot(scene, 1, "medium", "static", "35mm f/2.8",
                                0.0, mid, "Scene setup",
                                ["Character 1"],
                                "Establishing shot",
                                "cut", "cut"),
                self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                                mid, duration, "Character close-up",
                                ["Character 1"],
                                "Character expression",
                                "cut", "cut")
            ]

    def _build_dialogue_two(self, scene):
        """
        Build shots for a scene with two-character dialogue.

        Args:
            scene: Scene dictionary

        Returns:
            List of shot dictionaries
        """
        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                duration = 8.0

            characters = scene.get("characters", [])
            if not isinstance(characters, list):
                characters = []

            char_names = [c.get("name", f"Character {i+1}") for i, c in enumerate(characters) if isinstance(c, dict)]
            # Ensure we have at least two character names
            while len(char_names) < 2:
                char_names.append(f"Character {len(char_names)+1}")

            n_shots = max(2, min(4, int(duration / StoryboardAgent.MIN_SHOT_DURATION)))
            shot_duration = duration / n_shots
            shots = []

            if n_shots == 2:
                shots.append(self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                                            0.0, shot_duration, f"Ambos personajes en cuadro: {', '.join(char_names[:2])}",
                                            char_names[:2], "Relación espacial entre personajes",
                                            scene.get("transition", "cut"), "cut"))
                shots.append(self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                                            shot_duration, duration, f"Clímax: {char_names[0]} confronta a {char_names[1]}",
                                            [char_names[0]], "Momento culminante del diálogo",
                                            "cut", "cut"))
            else:
                shots.append(self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                                            0.0, shot_duration,
                                            f"Ambos personajes en cuadro: {', '.join(char_names[:2])}",
                                            char_names[:2], "Relación espacial entre personajes",
                                            scene.get("transition", "cut"), "cut"))
                shots.append(self._build_shot(scene, 2, "over-the-shoulder", "static", "35mm f/2.8",
                                            shot_duration, shot_duration * 2,
                                            f"Sobre el hombro de {char_names[0]}: {char_names[1]} reacciona",
                                            [char_names[0], char_names[1]], f"Reacción de {char_names[1]}",
                                            "cut", "cut"))
                if n_shots >= 3:
                    shots.append(self._build_shot(scene, 3, "over-the-shoulder", "static", "35mm f/2.8",
                                                shot_duration * 2, shot_duration * 3,
                                                f"Sobre el hombro de {char_names[1]}: {char_names[0]} responde",
                                                [char_names[0], char_names[1]], f"Respuesta de {char_names[0]}",
                                                "cut", "cut"))
                if n_shots >= 4:
                    shots.append(self._build_shot(scene, 4, "close-up", "slow push-in", "50mm f/2.0",
                                                shot_duration * 3, duration,
                                                f"Clímax: {char_names[0]} confronta a {char_names[1]}",
                                                [char_names[0], char_names[1]], "Momento culminante del diálogo",
                                                "cut", "cut"))

            return shots
        except Exception as e:
            logger.exception(f"Error building dialogue two shots: {e}")
            # Return fallback shots
            duration = scene.get("duration", 8.0) if isinstance(scene.get("duration"), (int, float)) and scene.get("duration") > 0 else 8.0
            shot_duration = duration / 2
            return [
                self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                                0.0, shot_duration, "Two characters in scene",
                                ["Character 1", "Character 2"],
                                "Establishing shot",
                                "cut", "cut"),
                self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                                shot_duration, duration, "Character interaction",
                                ["Character 1"],
                                "Character reaction",
                                "cut", "cut")
            ]

    def _build_action(self, scene):
        """
        Build shots for an action scene.

        Args:
            scene: Scene dictionary

        Returns:
            List of three shot dictionaries
        """
        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                duration = 8.0

            characters = scene.get("characters", [])
            if not isinstance(characters, list):
                characters = []

            n_shots = 3
            shot_duration = duration / n_shots
            return [
                self._build_shot(scene, 1, "wide", "tracking", "24mm f/4",
                                0.0, shot_duration, scene.get("description", ""),
                                [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                "Contexto de la acción",
                                scene.get("transition", "cut"), "cut"),
                self._build_shot(scene, 2, "medium", "tracking", "35mm f/2.8",
                                shot_duration, shot_duration * 2, f"Movimiento de {characters[0].get('name', 'Character') if characters and isinstance(characters, list) and len(characters) > 0 and isinstance(characters[0], dict) else 'personaje'} en acción",
                                [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                "Seguimiento del movimiento",
                                "cut", "cut"),
                self._build_shot(scene, 3, "close-up", "static", "50mm f/2.0",
                                shot_duration * 2, duration, "Impacto o efecto de la acción",
                                [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                "Momento de impacto",
                                "cut", "cut")
            ]
        except Exception as e:
            logger.exception(f"Error building action shots: {e}")
            # Return fallback shots
            duration = scene.get("duration", 8.0) if isinstance(scene.get("duration"), (int, float)) and scene.get("duration") > 0 else 8.0
            shot_duration = duration / 3
            return [
                self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                                0.0, shot_duration, "Action scene setup",
                                ["Character 1", "Character 2"],
                                "Establishing shot",
                                "cut", "cut"),
                self._build_shot(scene, 2, "medium", "static", "35mm f/2.8",
                                shot_duration, shot_duration * 2, "Action in progress",
                                ["Character 1", "Character 2"],
                                "Action continuation",
                                "cut", "cut"),
                self._build_shot(scene, 3, "close-up", "static", "50mm f/2.0",
                                shot_duration * 2, duration, "Action climax",
                                ["Character 1"],
                                "Action climax",
                                "cut", "cut")
            ]

    def _build_silent_mood(self, scene, mood):
        """
        Build shots for a silent/mood-based scene.

        Args:
            scene: Scene dictionary
            mood: Mood string

        Returns:
            List of shot dictionaries
        """
        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                duration = 8.0

            characters = scene.get("characters", [])
            if not isinstance(characters, list):
                characters = []

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
                                            [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                            f"Enfoque en {shot_type}: atmósfera {mood}",
                                            "cut" if i > 0 else scene.get("transition", "cut"), "cut"))
            return shots
        except Exception as e:
            logger.exception(f"Error building silent mood shots: {e}")
            # Return fallback shots
            duration = scene.get("duration", 8.0) if isinstance(scene.get("duration"), (int, float)) and scene.get("duration") > 0 else 8.0
            shot_duration = duration / 2
            return [
                self._build_shot(scene, 1, "wide", "static", "24mm f/4",
                                0.0, shot_duration, "Establishing shot",
                                [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                "Wide establishing shot",
                                "cut", "cut"),
                self._build_shot(scene, 2, "close-up", "slow push-in", "50mm f/2.0",
                                shot_duration, duration, "Close-up detail",
                                [c.get("name", "Unknown") for c in characters if isinstance(c, dict)],
                                "Important detail",
                                "cut", "cut")
            ]

    def _build_shot(self, scene, shot_number, shot_type, movement, lens,
                    start_time, end_time, description, characters_in_frame,
                    focus, transition_in, transition_out):
        """
        Build a single shot dictionary.

        Args:
            scene: Scene dictionary
            shot_number: Shot number (1-based)
            shot_type: Type of shot (e.g., "wide", "close-up")
            movement: Camera movement (e.g., "static", "tracking")
            lens: Lens specification (e.g., "35mm f/2.8")
            start_time: Start time in seconds
            end_time: End time in seconds
            description: Shot description
            characters_in_frame: List of character names in the shot
            focus: Focus point of the shot
            transition_in: Transition in type
            transition_out: Transition out type

        Returns:
            Shot dictionary
        """
        try:
            return {
                "shot_number": int(shot_number),
                "start_time": float(start_time),
                "end_time": float(end_time),
                "shot_type": str(shot_type),
                "movement": str(movement),
                "lens": str(lens),
                "description": str(description),
                "characters_in_frame": [str(c) for c in characters_in_frame] if isinstance(characters_in_frame, list) else [],
                "focus": str(focus),
                "transition_in": str(transition_in),
                "transition_out": str(transition_out),
                "slow_motion": bool(False),
                "lens_flare": bool(False),
                "dutch_angle": float(0),
                "director_style": None,
            }
        except Exception as e:
            logger.exception(f"Error building shot: {e}")
            # Return a minimal valid shot
            return {
                "shot_number": 1,
                "start_time": 0.0,
                "end_time": 8.0,
                "shot_type": "wide",
                "movement": "static",
                "lens": "35mm f/2.8",
                "description": "",
                "characters_in_frame": [],
                "focus": "",
                "transition_in": "cut",
                "transition_out": "cut",
                "slow_motion": False,
                "lens_flare": False,
                "dutch_angle": 0,
                "director_style": None,
            }

    def _build_action_styled(self, scene, config, style):
        """
        Build action shots with a specific director's style.

        Args:
            scene: Scene dictionary
            config: Director style configuration
            style: Director style name

        Returns:
            List of shot dictionaries
        """
        try:
            duration = scene.get("duration", 8.0)
            if not isinstance(duration, (int, float)) or duration <= 0:
                duration = 8.0

            characters = scene.get("characters", [])
            if not isinstance(characters, list):
                characters = []

            char_names = [c.get("name", f"Character {i+1}") for i, c in enumerate(characters) if isinstance(c, dict)]
            # Ensure we have at least one character name
            if not char_names:
                char_names = ["Character 1"]

            n_shots = min(4, max(3, int(duration / 3)))
            shot_duration = duration / n_shots
            shots = []

            preferred_shots = config.get("preferred_shot_types", ["wide", "medium", "close-up"])
            preferred_moves = config.get("preferred_movements", ["static", "tracking", "static"])
            slow_mo = config.get("slow_motion", {"enabled": False})
            lens_flare = config.get("lens_flare", False)
            dutch_angle = config.get("dutch_angle", 0)

            for i in range(n_shots):
                shot_type = preferred_shots[i % len(preferred_shots)]
                movement = preferred_moves[i % len(preferred_moves)]

                is_slow_mo = False
                shot_dur = shot_duration
                if isinstance(slow_mo, dict) and slow_mo.get("enabled", False):
                    is_slow_mo = (i == n_shots - 1)
                    if is_slow_mo:
                        slow_fps = slow_mo.get("fps", 24)
                        if isinstance(slow_fps, (int, float)) and slow_fps > 0:
                            slow_factor = min(slow_fps / 24, 2.0)  # Cap slowdown factor
                            max_duration = slow_mo.get("max_duration", 4.0)
                            if isinstance(max_duration, (int, float)) and max_duration > 0:
                                shot_dur = min(shot_duration * slow_factor, max_duration)
                            else:
                                shot_dur = shot_duration * slow_factor

                start = i * shot_duration
                end = start + shot_dur

                description = f"{scene.get('description', '')} — {shot_type.replace('_', ' ')} ({movement.replace('_', ' ')})"
                focus = f"Action beat {i + 1}: {shot_type}"

                shot = self._build_shot_styled(
                    scene, i + 1, shot_type, movement, start, end,
                    description, char_names, focus, style,
                    slow_mo=is_slow_mo, lens_flare=lens_flare, dutch_angle=dutch_angle,
                )
                shots.append(shot)

            return shots
        except Exception as e:
            logger.exception(f"Error building styled action shots: {e}")
            # Fallback to regular action shots
            return self._build_action(scene)

    def _build_shot_styled(self, scene, shot_number, shot_type, movement,
                           start_time, end_time, description, characters_in_frame,
                           focus, director_style, slow_mo=False, lens_flare=False,
                           dutch_angle=0):
        """
        Build a styled shot dictionary.

        Args:
            scene: Scene dictionary
            shot_number: Shot number (1-based)
            shot_type: Type of shot (e.g., "wide", "close-up")
            movement: Camera movement (e.g., "static", "tracking")
            start_time: Start time in seconds
            end_time: End time in seconds
            description: Shot description
            characters_in_frame: List of character names in the shot
            focus: Focus point of the shot
            director_style: Director style name
            slow_mo: Whether to use slow motion
            lens_flare: Whether to use lens flare
            dutch_angle: Dutch angle degrees

        Returns:
            Styled shot dictionary
        """
        try:
            lens = scene.get("camera", {}).get("lens", "35mm f/2.8")
            transition_in = "cut" if shot_number > 1 else scene.get("transition", "cut")
            transition_out = "cut"

            shot = self._build_shot(scene, shot_number, shot_type, movement, lens,
                                  start_time, end_time, description, characters_in_frame,
                                  focus, transition_in, transition_out)
            shot["slow_motion"] = bool(slow_mo)
            shot["lens_flare"] = bool(lens_flare)
            shot["dutch_angle"] = float(dutch_angle)
            shot["director_style"] = str(director_style) if director_style else None
            return shot
        except Exception as e:
            logger.exception(f"Error building styled shot: {e}")
            # Return a basic shot with the styling applied as best as possible
            return {
                "shot_number": int(shot_number) if isinstance(shot_number, (int, float)) and not isinstance(shot_number, bool) else 1,
                "start_time": float(start_time) if isinstance(start_time, (int, float)) else 0.0,
                "end_time": float(end_time) if isinstance(end_time, (int, float)) else 8.0,
                "shot_type": str(shot_type) if shot_type else "wide",
                "movement": str(movement) if movement else "static",
                "lens": "35mm f/2.8",
                "description": str(description) if description else "",
                "characters_in_frame": [str(c) for c in characters_in_frame] if isinstance(characters_in_frame, list) else [],
                "focus": str(focus) if focus else "",
                "transition_in": "cut",
                "transition_out": "cut",
                "slow_motion": bool(slow_mo),
                "lens_flare": bool(lens_flare),
                "dutch_angle": float(dutch_angle) if isinstance(dutch_angle, (int, float)) else 0.0,
                "director_style": str(director_style) if director_style else None,
            }

    def _is_action_scene(self, mood: str) -> bool:
        """
        Determine if a scene is an action scene based on mood.

        Args:
            mood: Mood string from scene lighting

        Returns:
            True if this is an action scene, False otherwise
        """
        if not isinstance(mood, str):
            return False
        return mood.lower() in ("intense", "epic", "dramatic", "explosive", "action", "chaotic")