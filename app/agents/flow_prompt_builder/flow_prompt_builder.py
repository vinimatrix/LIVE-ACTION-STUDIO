from typing import Dict, Any, List
from app.agents.storyboard.storyboard import StoryboardAgent


class FlowPromptBuilderAgent:
    def build_prompts(self, scenes: List[Dict[str, Any]], character_mapping: Dict[str, str]) -> List[Dict[str, Any]]:
        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            duration = scene.get("duration", 8.0)
            prompt_text = self._build_prompt(scene, character_mapping, i + 1, start_time)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": duration,
                "prompt_text": prompt_text
            })
            start_time += duration
        return prompts

    def _build_prompt(self, scene: Dict[str, Any], character_mapping: Dict[str, str], scene_num: int, start_time: float) -> str:
        duration = scene.get("duration", 8.0)
        end_time = start_time + duration

        lines = []
        lines.append(f"ESCENA {scene_num} ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
        lines.append("─" * 50)
        lines.append("")

        # PERSONAJES
        lines.append("PERSONAJES:")
        for c in scene.get("characters", []):
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
        lines.append(f"  - Descripci\u00f3n: {scene.get('description', '')}")
        lines.append(f"  - Hora: {time_of_day}")
        lines.append("")

        # CAMARA
        camera = scene.get("camera", {})
        lines.append("C\u00c1MARA:")
        lines.append(f"  - Shot: {camera.get('shot_type', 'wide')}")
        lines.append(f"  - Movimiento: {camera.get('movement', 'static')}")
        lines.append(f"  - Lente: {camera.get('lens', '35mm f/2.8')}")
        lines.append("")

        # ILUMINACION
        mood = lighting.get("mood_lighting", "neutral")
        lines.append("ILUMINACI\u00d3N:")
        lines.append(f"  - Ambiente: {time_of_day} lighting")
        lines.append(f"  - Mood: {mood}")
        lines.append("")

        # MOOD
        lines.append("MOOD: " + mood.capitalize())
        lines.append("")

        # ACCION
        lines.append("ACCI\u00d3N:")
        lines.append(f"  - {scene.get('description', '')}")
        lines.append(f"  - Duraci\u00f3n: {duration:.1f} segundos")
        for d in scene.get("dialogue", []):
            lines.append(f"  - Di\u00e1logo: [{d.get('character', '?')}] \"{d.get('text', '')}\"")
        lines.append("")

        # SPECS TECNICAS
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
            n = name.get("name", "")
            flow_ref = character_mapping.get(n, n)
            lines.append(f"  - Mantener consistencia total del diseño y rostro de {n} (ref: {flow_ref}) exactamente como en la referencia de Flow")
        lines.append("  - No alucinar ni añadir objetos, personajes o elementos no descritos")
        lines.append("  - Fondo coherente y consistente con la historia narrada y descripción del escenario")
        lines.append("  - Respetar iluminación y hora del día especificadas")
        lines.append("  - No cambiar expresiones faciales ni poses indicadas")

        return "\n".join(lines)

    def _fmt_time(self, seconds: float) -> str:
        m = int(seconds // 60)
        s = int(seconds % 60)
        return f"{m:02d}:{s:02d}"

    def build_storyboard_prompts(
        self,
        scenes: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        storyboard_agent: StoryboardAgent = None
    ) -> List[Dict[str, Any]]:
        if storyboard_agent is None:
            storyboard_agent = StoryboardAgent()

        prompts = []
        start_time = 0.0
        for i, scene in enumerate(scenes):
            duration = scene.get("duration", 8.0)
            shots = storyboard_agent.break_down_scene(scene)
            prompt_text = self._build_hybrid_prompt(scene, shots, character_mapping, i + 1, start_time)
            prompts.append({
                "scene_id": scene["scene_id"],
                "scene_number": i + 1,
                "duration": duration,
                "prompt_text": prompt_text
            })
            start_time += duration
        return prompts

    def _build_hybrid_prompt(
        self,
        scene: Dict[str, Any],
        shots: List[Dict[str, Any]],
        character_mapping: Dict[str, str],
        scene_num: int,
        start_time: float
    ) -> str:
        duration = scene.get("duration", 8.0)
        end_time = start_time + duration
        lines = []

        # GLOBAL CONTEXT BLOCK
        lines.append(f"ESCENA {scene_num} — Contexto Global ({self._fmt_time(start_time)} - {self._fmt_time(end_time)})")
        lines.append("─" * 70)
        lines.append("")
        lines.append("PERSONAJES:")
        for c in scene.get("characters", []):
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
            shot_start = self._fmt_time(shot["start_time"])
            shot_end = self._fmt_time(shot["end_time"])
            shot_type = shot["shot_type"].replace("_", " ").title()
            movement = shot["movement"].replace("_", " ").title()
            lines.append(f"╔══ SHOT {shot['shot_number']} ({shot_start} → {shot_end}) ═══════════════════════════════════════")
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
            lines.append("║")
            lines.append("║  ANTI-ALUCINACIÓN (shot específico):")
            lines.append(f"║    - Mantener exactamente este encuadre: {shot_type}, {movement}")
            if shot["characters_in_frame"]:
                lines.append(f"║    - Solo {', '.join(shot['characters_in_frame'])} visible(s) en este shot")
                for char_name in shot["characters_in_frame"]:
                    expr = next((c.get("expression", "neutral") for c in scene.get("characters", [])
                                 if c["name"] == char_name), "neutral")
                    lines.append(f"║    - No cambiar expresión de {char_name}: {expr}")
            lines.append(f"╚══ FIN SHOT {shot['shot_number']} {'═' * 50}")
            lines.append("")

        return "\n".join(lines)
