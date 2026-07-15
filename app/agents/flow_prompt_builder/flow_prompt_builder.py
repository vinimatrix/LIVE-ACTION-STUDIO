from typing import Dict, Any, List, Optional
from app.agents.storyboard.storyboard import StoryboardAgent
from app.agents.director_styles import DIRECTOR_STYLES, resolve_style
import logging

logger = logging.getLogger(__name__)


class FlowPromptBuilderAgent:
    def build_prompts(self, scenes: List[Dict[str, Any]], character_mapping: Dict[str, str],
                      director_style: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Build prompts for a list of scenes.

        Args:
            scenes: List of scene dictionaries
            character_mapping: Mapping from character names to Flow references
            director_style: Optional director style to apply

        Returns:
            List of prompt dictionaries with scene_id, scene_number, duration, and prompt_text

        Raises:
            TypeError: If scenes is not a list or character_mapping is not a dict
        """
        if not isinstance(scenes, list):
            logger.error(f"Expected list for scenes, got {type(scenes)}")
            raise TypeError(f"scenes must be a list, got {type(scenes)}")

        if not isinstance(character_mapping, dict):
            logger.error(f"Expected dict for character_mapping, got {type(character_mapping)}")
            raise TypeError(f"character_mapping must be a dictionary, got {type(character_mapping)}")

        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            if not isinstance(scene, dict):
                logger.warning(f"Skipping invalid scene at index {i}: {scene}")
                continue

            try:
                duration = scene.get("duration", 8.0)
                if not isinstance(duration, (int, float)) or duration <= 0:
                    logger.warning(f"Invalid duration for scene {scene.get('scene_id', i)}: {duration}, using default 8.0")
                    duration = 8.0

                prompt_text = self._build_prompt(scene, character_mapping, i + 1, start_time, director_style)
                prompts.append({
                    "scene_id": scene.get("scene_id", f"scene_{i+1}"),
                    "scene_number": i + 1,
                    "duration": float(duration),
                    "prompt_text": prompt_text
                })
                start_time += duration
            except Exception as e:
                logger.exception(f"Error building prompt for scene {scene.get('scene_id', i)}: {e}")
                # Skip this scene rather than failing the entire batch
                continue

        return prompts

    def _build_prompt(self, scene: Dict[str, Any], character_mapping: Dict[str, str], scene_num: int, start_time: float,
                      director_style: Optional[str] = None) -> str:
        """
        Build a prompt for a single scene.

        Args:
            scene: Scene dictionary
            character_mapping: Mapping from character names to Flow references
            scene_num: Scene number (1-based)
            start_time: Start time in seconds
            director_style: Optional director style to apply

        Returns:
            Formatted prompt string
        """
        try:
            duration = scene.get("duration", 8.0)
            end_time = start_time + duration

            lines = []
            lines.append(f"ESCENA {scene_num} ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
            lines.append("─" * 50)
            lines.append("")

            # PERSONAJES
            lines.append("PERSONAJES:")
            for c in scene.get("characters", []):
                if not isinstance(c, dict):
                    logger.warning(f"Skipping invalid character data: {c}")
                    continue

                name = c.get("name", "Unknown")
                flow_ref = character_mapping.get(name, name)
                appearance = c.get("appearance", "")
                expression = c.get("expression", "neutral")
                position = c.get("position", "frame")
                lines.append(f"  - {name} (Flow ref: {flow_ref}): {expression}, {position}")
                if appearance:
                    lines.append(f"    Apariencia: {appearance}")
            lines.append("")

            # ESCENARIO
            lines.append("ESCENARIO:")
            lighting = scene.get("lighting", {})
            time_of_day = lighting.get("time_of_day", "day")
            lines.append(f"  - Descripción: {scene.get('description', '')}")
            lines.append(f"  - Hora: {time_of_day}")
            lines.append("")

            # CÁMARA
            camera = scene.get("camera", {})
            lines.append("CÁMARA:")
            lines.append(f"  - Shot: {camera.get('shot_type', 'wide')}")
            lines.append(f"  - Movimiento: {camera.get('movement', 'static')}")
            lines.append(f"  - Lente: {camera.get('lens', '35mm f/2.8')}")
            lines.append("")

            # ILUMINACIÓN
            mood = lighting.get("mood_lighting", "neutral")
            lines.append("ILUMINACIÓN:")
            lines.append(f"  - Ambiente: {time_of_day} lighting")
            lines.append(f"  - Mood: {mood}")
            lines.append("")

            # MOOD
            lines.append("MOOD: " + mood.capitalize())
            lines.append("")

            # ACCIÓN
            lines.append("ACCIÓN:")
            lines.append(f"  - {scene.get('description', '')}")
            lines.append(f"  - Duración: {duration:.1f} segundos")
            for d in scene.get("dialogue", []):
                if not isinstance(d, dict):
                    logger.warning(f"Skipping invalid dialogue data: {d}")
                    continue
                lines.append(f"  - Diálogo: [{d.get('character', '?')}] \"{d.get('text', '')}\"")
            lines.append("")

            # DIRECCIÓN
            if director_style:
                mood_val = scene.get("lighting", {}).get("mood_lighting", "neutral")
                style = resolve_style(director_style, mood_val)
                config = DIRECTOR_STYLES.get(style)
                if config:
                    style_name = style.replace("_", " ").title()
                    lines.append("DIRECCIÓN:")
                    lines.append(f"  - Estilo: {style_name}")
                    if config.get("lens_flare"):
                        lines.append("  - Flares: Activados (anamórficos)")
                    if config.get("dutch_angle", 0) > 0:
                        lines.append(f"  - Dutch angle: {config['dutch_angle']}°")
                    if config.get("color_grading"):
                        grading_name = config["color_grading"].replace("_", " ").title()
                        lines.append(f"  - Color grading: {grading_name}")
                    lines.append("")

            # SPECS TÉCNICAS
            lines.append("SPECS TÉCNICAS:")
            lines.append("  - Resolución: 8K (7680x4320)")
            lines.append("  - Estilo: live-action hiperrealista, cinematográfico, fotorrealista")
            lines.append("  - Texturas: extremadamente detalladas, poros de la piel realistas, texturas PBR")
            lines.append("  - Iluminación: volumetric lighting, cinematic lighting, global illumination")
            lines.append("  - Post-procesado: color grading cinematográfico, grain sutil de película analógica, sin CGI, sin renderizado 3D")
            lines.append("  - Motion blur: obturador 180°, movimiento realista natural")
            lines.append("  - Profundidad de campo: acorde al shot, f/1.8 o f/2.8 característico")
            lines.append("")

            # ANTI-ALUCINACIÓN
            lines.append("ANTI-ALUCINACIÓN:")
            for name in scene.get("characters", []):
                if not isinstance(name, dict):
                    logger.warning(f"Skipping invalid character data in anti-alucination: {name}")
                    continue
                n = name.get("name", "")
                flow_ref = character_mapping.get(n, n)
                lines.append(f"  - Mantener consistencia total del diseño y rostro de {n} (ref: {flow_ref}) exactamente como en la referencia de Flow")
            lines.append("  - No alucinar ni añadir objetos, personajes o elementos no descritos")
            lines.append("  - Fondo coherente y consistente con la historia narrada y descripción del escenario")
            lines.append("  - Respetar iluminación y hora del día especificadas")
            lines.append("  - No cambiar expresiones faciales ni poses indicadas")

            return "\n".join(lines)
        except Exception as e:
            logger.exception(f"Error building prompt for scene {scene.get('scene_id', 'unknown')}: {e}")
            # Return a basic fallback prompt
            return f"""ESCENA {scene_num} ({self._fmt_time(start_time)} - {self._fmt_time(start_time + scene.get('duration', 8.0))})
──────────────────
PERSONAJES:
  - Información de personajes no disponible

ESCENARIO:
  - Descripción: {scene.get('description', 'Descripción no disponible')}
  - Hora: day

CÁMARA:
  - Shot: wide
  - Movimiento: static
  - Lente: 35mm f/2.8

ILUMINACIÓN:
  - Ambiente: day lighting
  - Mood: neutral

MOOD: Neutral

ACCIÓN:
  - {scene.get('description', 'Descripción no disponible')}
  - Duración: {scene.get('duration', 8.0):.1f} segundos

SPECS TÉCNICAS:
  - Resolución: 8K (7680x4320)
  - Estilo: live-action hiperrealista, cinematográfico, fotorrealista
  - Texturas: extremadamente detalladas, poros de la piel realistas, texturas PBR
  - Iluminación: volumetric lighting, cinematic lighting, global illumination
  - Post-procesado: color grading cinematográfico, grain sutil de película analógica, sin CGI, sin renderizado 3D
  - Motion blur: obturador 180°, movimiento realista natural
  - Profundidad de campo: acorde al shot, f/1.8 o f/2.8 característico

ANTI-ALUCINACIÓN:
  - Mantener consistencia total del diseño y rostro de los personajes exactamente como en la referencia de Flow
  - No alucinar ni añadir objetos, personajes o elementos no descritos
  - Fondo coherente y consistente con la historia narrada y descripción del escenario
  - Respetar iluminación y hora del día especificadas
  - No cambiar expresiones faciales ni poses indicadas"""

    def _fmt_time(self, seconds: float) -> str:
        """
        Format seconds as MM:SS.

        Args:
            seconds: Time in seconds

        Returns:
            Formatted time string as MM:SS
        """
        try:
            if not isinstance(seconds, (int, float)):
                raise ValueError(f"Seconds must be a number, got {type(seconds)}")

            m = int(seconds // 60)
            s = int(seconds % 60)
            return f"{m:02d}:{s:02d}"
        except Exception as e:
            logger.exception(f"Error formatting time {seconds}: {e}")
            return "00:00"

    def build_storyboard_prompts(
        self,
        scenes: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        storyboard_agent: StoryboardAgent = None,
        director_style: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Build storyboard prompts for a list of scenes.

        Args:
            scenes: List of scene dictionaries
            character_mapping: Mapping from character names to Flow references
            storyboard_agent: StoryboardAgent instance (optional)
            director_style: Optional director style to apply

        Returns:
            List of prompt dictionaries with scene_id, scene_number, duration, and prompt_text

        Raises:
            TypeError: If scenes is not a list or character_mapping is not a dict
        """
        if not isinstance(scenes, list):
            logger.error(f"Expected list for scenes, got {type(scenes)}")
            raise TypeError(f"scenes must be a list, got {type(scenes)}")

        if not isinstance(character_mapping, dict):
            logger.error(f"Expected dict for character_mapping, got {type(character_mapping)}")
            raise TypeError(f"character_mapping must be a dictionary, got {type(character_mapping)}")

        if storyboard_agent is None:
            storyboard_agent = StoryboardAgent()

        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            if not isinstance(scene, dict):
                logger.warning(f"Skipping invalid scene at index {i}: {scene}")
                continue

            try:
                duration = scene.get("duration", 8.0)
                if not isinstance(duration, (int, float)) or duration <= 0:
                    logger.warning(f"Invalid duration for scene {scene.get('scene_id', i)}: {duration}, using default 8.0")
                    duration = 8.0

                shots = storyboard_agent.break_down_scene(scene, director_style=director_style)
                prompt_text = self._build_hybrid_prompt(scene, shots, character_mapping, i + 1, start_time, director_style)
                prompts.append({
                    "scene_id": scene.get("scene_id", f"scene_{i+1}"),
                    "scene_number": i + 1,
                    "duration": float(duration),
                    "prompt_text": prompt_text
                })
                start_time += duration
            except Exception as e:
                logger.exception(f"Error building storyboard prompt for scene {scene.get('scene_id', i)}: {e}")
                # Skip this scene rather than failing the entire batch
                continue

        return prompts

    def _build_hybrid_prompt(
        self,
        scene: Dict[str, Any],
        shots: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        scene_num: int,
        start_time: float,
        director_style: Optional[str] = None
    ) -> str:
        """
        Build a hybrid prompt combining scene description with storyboard shots.

        Args:
            scene: Scene dictionary
            shots: List of shot dictionaries from storyboard
            character_mapping: Mapping from character names to Flow references
            scene_num: Scene number (1-based)
            start_time: Start time in seconds
            director_style: Optional director style to apply

        Returns:
            Formatted prompt string
        """
        try:
            duration = scene.get("duration", 8.0)
            end_time = start_time + duration
            lines = []

            # GLOBAL CONTEXT BLOCK
            lines.append(f"ESCENA {scene_num} — Contexto Global ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
            lines.append("─" * 70)
            lines.append("")
            lines.append("PERSONAJES:")
            for c in scene.get("characters", []):
                if not isinstance(c, dict):
                    logger.warning(f"Skipping invalid character data in global context: {c}")
                    continue
                name = c.get("name", "Unknown")
                flow_ref = character_mapping.get(name, name)
                expression = c.get("expression", "neutral")
                lines.append(f"  - {name} (Flow ref: {flow_ref}): {expression}")
            lines.append("")
            lines.append("ESCENARIO:")
            lighting = scene.get("lighting", {})
            lines.append(f"  - Descripción: {scene.get('description', '')}")
            lines.append(f"  - Hora: {lighting.get('time_of_day', 'day')}")
            lines.append(f"  - Mood: {lighting.get('mood_lighting', 'neutral')}")
            lines.append("")
            dialogue = scene.get("dialogue", [])
            if dialogue:
                lines.append("DIÁLOGO:")
                for d in dialogue:
                    if not isinstance(d, dict):
                        logger.warning(f"Skipping invalid dialogue data: {d}")
                        continue
                    lines.append(f"  - [{d.get('character', '?')}] \"{d.get('text', '')}\"")
                lines.append("")
            lines.append("SPECS TÉCNICAS:")
            lines.append("  - Resolución: 8K (7680x4320)")
            lines.append("  - Estilo: live-action hiperrealista, cinematográfico, fotorrealista")
            lines.append("  - Texturas: extremadamente detalladas, poros de la piel realistas, texturas PBR")
            lines.append("  - Iluminación: volumetric lighting, cinematic lighting, global illumination")
            lines.append("  - Post-procesado: color grading cinematográfico, grain sutil de película analógica, sin CGI, sin renderizado 3D")
            lines.append("  - Motion blur: obturador 180°, movimiento realista natural")
            lines.append("")
            lines.append("ANTI-ALUCINACIÓN (global):")
            for c in scene.get("characters", []):
                if not isinstance(c, dict):
                    logger.warning(f"Skipping invalid character data in anti-alucination global: {c}")
                    continue
                name = c.get("name", "")
                flow_ref = character_mapping.get(name, name)
                lines.append(f"  - Mantener consistencia total de {name} (ref: {flow_ref}) exactamente como en la referencia de Flow")
            lines.append("  - No alucinar ni añadir objetos, personajes o elementos no descritos")
            lines.append("  - Fondo coherente con la descripción del escenario en todos los shots")
            lines.append("  - Respetar iluminación y hora del día especificadas")
            lines.append("")

            # STORYBOARD SHOTS
            lines.append("STORYBOARD:")
            lines.append("")
            for shot in shots:
                if not isinstance(shot, dict):
                    logger.warning(f"Skipping invalid shot data: {shot}")
                    continue

                try:
                    shot_start = self._fmt_time(shot["start_time"])
                    shot_end = self._fmt_time(shot["end_time"])
                    shot_type = shot["shot_type"].replace("_", " ").title()
                    movement = shot["movement"].replace("_", " ").title()
                    lines.append(f"╔══ SHOT {shot['shot_number']} ({shot_start} → {shot_end}) ══════════════════════════════════════")
                    lines.append(f"║  TIPO: {shot_type}")
                    lines.append(f"║  MOV: {movement}")
                    lines.append(f"║  LENTE: {shot['lens']}")
                    lines.append(f"║  TRANSICIÓN IN: {shot['transition_in'].replace('_', ' ').title()}")
                    lines.append(f"║  TRANSICIÓN OUT: {shot['transition_out'].replace('_', ' ').title()}")
                    lines.append("║")
                    lines.append(f"║  PERSONAJES EN CUADRO:")
                    for char_name in shot["characters_in_frame"]:
                        flow_ref = character_mapping.get(char_name, char_name)
                        lines.append(f"║    - {char_name} (ref: {flow_ref})")
                    lines.append("║")
                    lines.append(f"║  ACCIÓN: {shot['description']}")
                    lines.append(f"║  FOCO: {shot['focus']}")
                    if shot.get("slow_motion"):
                        lines.append(f"║  SLOW-MO: ✅")
                    if shot.get("lens_flare"):
                        lines.append("║  FLARE: ✅")
                    if shot.get("dutch_angle", 0) > 0:
                        lines.append(f"║  DUTCH ANGLE: {shot['dutch_angle']}°")
                    lines.append("║")
                    lines.append("║  ANTI-ALUCINACIÓN (shot específico):")
                    lines.append(f"║    - Mantener exactamente este encuadre: {shot_type}, {movement}")
                    if shot["characters_in_frame"]:
                        lines.append(f"║    - Solo {', '.join(shot['characters_in_frame'])} visible(s) en este shot")
                        for char_name in shot["characters_in_frame"]:
                            expr = next((c.get("expression", "neutral") for c in scene.get("characters", [])
                                         if c.get("name") == char_name), "neutral")
                            lines.append(f"║    - No cambiar expresión de {char_name}: {expr}")
                    lines.append(f"╚══ FIN SHOT {shot['shot_number']} {'═' * 50}")
                    lines.append("")
                except Exception as e:
                    logger.exception(f"Error processing shot {shot.get('shot_number', 'unknown')}: {e}")
                    # Skip this shot but continue with others
                    continue

            return "\n".join(lines)
        except Exception as e:
            logger.exception(f"Error building hybrid prompt for scene {scene.get('scene_id', 'unknown')}: {e}")
            # Return a basic fallback prompt
            return f"""ESCENA {scene_num} — Contexto Global ({self._fmt_time(start_time)} - {self._fmt_time(start_time + scene.get('duration', 8.0))})
────────────────────────────────────────────────────────────────────
PERSONAJES:
  - Información de personajes no disponible

ESCENARIO:
  - Descripción: {scene.get('description', 'Descripción no disponible')}
  - Hora: day
  - Mood: neutral

SPECS TÉCNICAS:
  - Resolución: 8K (7680x4320)
  - Estilo: live-action hiperrealista, cinematográfico, fotorrealista
  - Texturas: extremadamente detalladas, poros de la piel realistas, texturas PBR
  - Iluminación: volumetric lighting, cinematic lighting, global illumination
  - Post-procesado: color grading cinematográfico, grain sutil de película analógica, sin CGI, sin renderizado 3D
  - Motion blur: obturador 180°, movimiento realista natural

ANTI-ALUCINACIÓN (global):
  - Mantener consistencia total de los personajes exactamente como en la referencia de Flow
  - No alucinar ni añadir objetos, personajes o elementos no descritos
  - Fondo coherente con la descripción del escenario en todos los shots
  - Respetar iluminación y hora del día especificadas

STORYBOARD:
  - Información de storyboard no disponible debido a un error en el procesamiento"""