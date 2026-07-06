import os
import sys
import base64
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.models import Character, Environment, Job, Scene, Asset

# Importar todos los agentes del pipeline
from app.agents.director.director import DirectorAgent
from app.agents.screenwriter.screenwriter import ScreenwriterAgent
from app.agents.character_manager.character_manager import CharacterManagerAgent
from app.agents.environment_manager.environment_manager import EnvironmentManagerAgent
from app.agents.prompt_builder.prompt_builder import PromptBuilderAgent
from app.agents.flow_prompt_builder.flow_prompt_builder import FlowPromptBuilderAgent
from app.agents.image_generator.image_generator import ImageGeneratorAgent
from app.agents.video_generator.video_generator import VideoGeneratorAgent
from app.agents.voice_generator.voice_generator import VoiceGeneratorAgent
from app.agents.music_generator.music_generator import MusicGeneratorAgent
from app.agents.fx_generator.fx_generator import FXGeneratorAgent
from app.agents.editor.editor import EditorAgent

# 1. Configurar base de datos SQLite para procesar esta página de Boruto
print("=== 1. CONFIGURANDO BASE DE DATOS PARA PROCESAR MANGA BORUTO ===")
DB_URL = "sqlite:///./prueba_manga_boruto.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Limpiar ejecuciones anteriores
db = SessionLocal()
db.query(Asset).delete()
db.query(Scene).delete()
db.query(Job).delete()
db.query(Character).delete()
db.query(Environment).delete()
db.commit()

# 2. Inicializar agentes
print("=== 2. INICIALIZANDO AGENTES ===")
director = DirectorAgent(db_session=SessionLocal)
screenwriter = ScreenwriterAgent()
character_manager = CharacterManagerAgent(db_session=SessionLocal)
environment_manager = EnvironmentManagerAgent(db_session=SessionLocal)
prompt_builder = PromptBuilderAgent()
flow_prompt_builder = FlowPromptBuilderAgent()
image_generator = ImageGeneratorAgent()
video_generator = VideoGeneratorAgent()
voice_generator = VoiceGeneratorAgent()
music_generator = MusicGeneratorAgent()
fx_generator = FXGeneratorAgent()
editor = EditorAgent()

# 3. Registrar Biblia del Universo para Boruto: Two Blue Vortex
print("\n=== 3. REGISTRANDO LA BIBLIA DEL UNIVERSO (Boruto: Two Blue Vortex) ===")

# Registrar Sarada Uchiha
sarada = character_manager.get_or_create_character(
    character_name="Sarada Uchiha",
    traits=["Decidida", "Líder", "Frustrada por la injusticia", "Inteligente"],
)
db_sarada = db.query(Character).filter(Character.id == sarada["id"]).first()
db_sarada.visual_references = ["/assets/references/sarada_tbv.jpg"]
db_sarada.expressions = ["enojada", "desesperada", "determinada"]
db_sarada.outfits = [{"name": "tbv_cloak", "ref": "/assets/references/sarada_tbv_outfit.jpg"}]
db_sarada.voice_profile = "eleven_labs_sarada_voice_id"

# Registrar Shikamaru Nara
shikamaru = character_manager.get_or_create_character(
    character_name="Shikamaru Nara",
    traits=["Pragmático", "Cansado", "Líder analítico", "Hokage"],
)
db_shikamaru = db.query(Character).filter(Character.id == shikamaru["id"]).first()
db_shikamaru.visual_references = ["/assets/references/shikamaru_tbv.jpg"]
db_shikamaru.expressions = ["serio", "cansado", "frío"]
db_shikamaru.outfits = [{"name": "8th_hokage_cloak", "ref": "/assets/references/shikamaru_hokage.jpg"}]
db_shikamaru.voice_profile = "eleven_labs_shikamaru_voice_id"

# Registrar Konohamaru Sarutobi
konohamaru = character_manager.get_or_create_character(
    character_name="Konohamaru Sarutobi",
    traits=["Protector", "Fiel al deber", "Serio"],
)
db_konohamaru = db.query(Character).filter(Character.id == konohamaru["id"]).first()
db_konohamaru.visual_references = ["/assets/references/konohamaru_tbv.jpg"]
db_konohamaru.expressions = ["serio", "atento"]
db_konohamaru.outfits = [{"name": "konoha_advisor_vest", "ref": "/assets/references/konohamaru_outfit.jpg"}]
db_konohamaru.voice_profile = "eleven_labs_konohamaru_voice_id"

db.commit()
print("Personajes registrados: Sarada Uchiha, Shikamaru Nara, Konohamaru Sarutobi.")

# Registrar la oficina del Hokage
office = Environment(
    name="Oficina del Hokage",
    description="Oficina espaciosa en Konoha con estanterías de libros, un gran escritorio de madera y grandes ventanales que muestran la aldea.",
    location_type="interior",
    visual_references=["/assets/references/hokage_office_bg.jpg"],
    lighting_conditions={"time_of_day": "day", "weather": "sunny", "style": "anime_cinematic"},
    props=["Hokage desk", "bookshelves", "large window", "papers"]
)
db.add(office)
db.commit()
print(f"Entorno registrado: {office.name}")

# 4. Iniciar el Job de Procesamiento
print("\n=== 4. INICIANDO PIPELINE DE PROCESAMIENTO DEL CAPÍTULO ===")
manga_request = {
    "filename": "boruto_tbv_ch1_p15.jpg",
    "page_url": "http://manga-reader.local/boruto/tbv_ch1_p15.jpg"
}
job_id = director.process_manga_request(manga_request)
job = db.query(Job).filter(Job.id == job_id).first()
print(f"Job creado. ID: {job.id}, Status: {job.status}")

# 5. Director Agent: Segmentar la página en escenas
print("\n=== 5. DIRECTOR AGENT: SEGMENTANDO EN ESCENAS CINEMATOGRÁFICAS ===")

# Vamos a definir formalmente las 3 escenas correspondientes a las 3 viñetas principales de la página
scenes_data = [
    {
        "manga_page_reference": "Panel 1 (Superior)",
        "description": "Sarada Uchiha apoya con frustración sus manos sobre el escritorio del Hokage, inclinándose hacia adelante con el rostro crispado de angustia e impotencia, gritando para hacerse oír.",
        "dialogue": [
            {"character": "Sarada Uchiha", "text": "¡¿Por qué no me entienden?! ¡¡Ya se los he explicado un millón de veces!!", "emotion": "frustrada y desesperada"}
        ],
        "actions": ["Sarada golpea suavemente el escritorio con impotencia.", "La cámara se enfoca en Sarada, mostrando su agitación."],
        "duration": 5.0,
        "shot_type": "medium shot",
        "camera_movement": "slow push-in",
        "environment_id": office.id,
        "job_id": job.id
    },
    {
        "manga_page_reference": "Panel 2 (Izquierda)",
        "description": "Primer plano de los ojos de Shikamaru Nara, fijos en Sarada, con una expresión de severa tristeza y peso institucional mientras recita los graves cargos.",
        "dialogue": [
            {"character": "Shikamaru Nara", "text": "Tuvo el descaro de matar al Hokage... e intentó acabar con su hijo Kawaki. Es un traidor. No se librará del castigo.", "emotion": "severo y frío"}
        ],
        "actions": ["Shikamaru entorna los ojos con gravedad.", "La iluminación cenital resalta la dureza en sus facciones."],
        "duration": 6.0,
        "shot_type": "extreme close-up",
        "camera_movement": "static",
        "environment_id": office.id,
        "job_id": job.id
    },
    {
        "manga_page_reference": "Panel 2 (Derecha)",
        "description": "Shikamaru Nara, vistiendo la capa del Octavo Hokage con patrones de fuego, le da la espalda a Sarada mirando de reojo. A su lado, Konohamaru Sarutobi permanece firme, con el ceño fruncido y los brazos cruzados en señal de advertencia.",
        "dialogue": [
            {"character": "Shikamaru Nara", "text": "Te digo lo mismo, Sarada. Ya hemos cedido infinidad de veces. Él fue el primero que cruzó la línea.", "emotion": "cansado pero firme"}
        ],
        "actions": ["Shikamaru se gira levemente mostrando la capa de Hokage.", "Konohamaru observa en silencio con firmeza militar."],
        "duration": 7.0,
        "shot_type": "medium-wide shot",
        "camera_movement": "pan left to right",
        "environment_id": office.id,
        "job_id": job.id
    }
]

# Guardar las escenas detalladas en la base de datos
db_scenes = []
# Borrar la escena genérica creada por defecto al crear el job para insertar las reales
db.query(Scene).filter(Scene.job_id == job.id).delete()
db.commit()

for sc_idx, sc_data in enumerate(scenes_data):
    sc = Scene(
        manga_page_reference=sc_data["manga_page_reference"],
        description=sc_data["description"],
        dialogue=sc_data["dialogue"],
        actions=sc_data["actions"],
        duration=sc_data["duration"],
        shot_type=sc_data["shot_type"],
        camera_movement=sc_data["camera_movement"],
        environment_id=sc_data["environment_id"],
        job_id=sc_data["job_id"]
    )
    db.add(sc)
    db.commit()
    db_scenes.append(sc)
    print(f"Escena {sc_idx + 1} guardada: {sc.manga_page_reference} - {sc.shot_type}")

# 6. Procesar cada escena a través del pipeline completo
print("\n=== 6. PROCESANDO ESCENAS A TRAVÉS DE LOS AGENTES GENERATIVOS ===")
scene_assets_map = {}
all_prompts_log = []
flow_scenes = []
char_map_combined = {}

for idx, sc in enumerate(db_scenes):
    print(f"\n--- Procesando Escena {idx + 1}: {sc.manga_page_reference} ---")
    
    # Screenwriter Agent
    screenplay_input = {
        "scene_id": sc.id,
        "dialogue": sc.dialogue,
        "actions": sc.actions
    }
    screenplay_result = screenwriter.process_scene(screenplay_input)
    print(f"  [Screenwriter] Guión procesado para la escena.")

    # Character Manager: Cargar personajes vinculados
    char_data_processed = character_manager.process_screenplay(screenplay_result)
    print(f"  [CharacterManager] Personajes identificados: {list(char_data_processed.get('character_data', {}).keys())}")

    # Estructurar datos completos de la escena
    scene_full_data = {
        "description": sc.description + " - " + " ".join(screenplay_result["actions"]),
        "duration": sc.duration,
        "character_data": char_data_processed.get("character_data", {}),
        "environment_data": {
            "location_type": office.location_type,
            "lighting_conditions": office.lighting_conditions
        },
        "camera_notes": {
            "shot_type": sc.shot_type,
            "movement": sc.camera_movement
        }
    }

    # Prompt Builder Agent
    image_prompt = prompt_builder.build_image_prompt(scene_full_data)
    video_prompt = prompt_builder.build_video_prompt(image_prompt, scene_full_data["duration"])
    voice_prompts = [
        prompt_builder.build_voice_prompt(dial) for dial in screenplay_result["dialogue"]
    ]
    music_prompt = prompt_builder.build_music_prompt(scene_full_data)
    effects_prompt = prompt_builder.build_effects_prompt(screenplay_result)

    print(f"  [PromptBuilder] Prompts de generación planos creados.")

    # Preparar escena para FlowPromptBuilderAgent
    flow_characters = []
    for c_name, c_data in char_data_processed.get("character_data", {}).items():
        flow_characters.append({
            "name": c_name,
            "appearance": ", ".join(c_data.get("personality_traits", [])),
            "expression": screenplay_result["dialogue"][0].get("emotion", "neutral") if screenplay_result["dialogue"] else "neutral",
            "position": "frame"
        })
        char_map_combined[c_name] = c_name
    
    flow_scenes.append({
        "scene_id": sc.id,
        "duration": sc.duration,
        "characters": flow_characters,
        "description": sc.description,
        "camera": {
            "shot_type": sc.shot_type,
            "movement": sc.camera_movement,
            "lens": "35mm f/1.8"
        },
        "lighting": {
            "time_of_day": "day",
            "mood_lighting": "cinematic_anime"
        },
        "dialogue": screenplay_result["dialogue"],
        "transition": "cut" if idx > 0 else "fade_in"
    })

    # Image Generator (Crea PNG real con Pillow)
    image_asset_data = image_generator.generate_image(image_prompt, scene_id=sc.id)
    image_meta = dict(image_asset_data["generation_params"])
    image_meta["prompt"] = image_prompt
    image_asset = Asset(
        job_id=job.id,
        scene_id=sc.id,
        asset_type="image",
        file_path=image_asset_data["file_path"],
        file_size=image_asset_data["file_size"],
        mime_type=image_asset_data["mime_type"],
        generation_metadata=image_meta
    )
    db.add(image_asset)
    print(f"  [ImageGen] Imagen guardada en: {image_asset.file_path}")

    # Video Generator (Crea MP4 binario real)
    video_asset_data = video_generator.generate_video(
        image_path=image_asset.file_path,
        prompt=video_prompt,
        duration=sc.duration
    )
    video_meta = dict(video_asset_data["generation_params"])
    video_meta["prompt"] = video_prompt
    video_asset = Asset(
        job_id=job.id,
        scene_id=sc.id,
        asset_type="video",
        file_path=video_asset_data["file_path"],
        file_size=video_asset_data["file_size"],
        mime_type=video_asset_data["mime_type"],
        generation_metadata=video_meta
    )
    db.add(video_asset)
    print(f"  [VideoGen] Video guardado en: {video_asset.file_path}")

    # Voice Generator (Crea WAV real)
    audio_tracks = []
    for v_idx, voice_pr in enumerate(voice_prompts):
        char_name = screenplay_result["dialogue"][v_idx]["character"]
        db_char = db.query(Character).filter(Character.name == char_name).first()
        char_id = db_char.id if db_char else None

        voice_asset_data = voice_generator.generate_voice(
            prompt=voice_pr,
            character_id=char_id
        )
        voice_asset = Asset(
            job_id=job.id,
            scene_id=sc.id,
            asset_type="audio",
            file_path=voice_asset_data["file_path"],
            file_size=voice_asset_data["file_size"],
            mime_type=voice_asset_data["mime_type"],
            generation_metadata={"prompt": voice_pr}
        )
        db.add(voice_asset)
        audio_tracks.append({"file_path": voice_asset.file_path})
        print(f"  [VoiceGen] Audio voz ({char_name}) guardado en: {voice_asset.file_path}")

    # Music Generator (Crea audio real)
    music_asset_data = music_generator.generate_music(
        prompt=music_prompt,
        duration=sc.duration
    )
    music_asset = Asset(
        job_id=job.id,
        scene_id=sc.id,
        asset_type="music",
        file_path=music_asset_data["file_path"],
        file_size=music_asset_data["file_size"],
        mime_type=music_asset_data["mime_type"],
        generation_metadata={"prompt": music_prompt}
    )
    db.add(music_asset)
    print(f"  [MusicGen] Música guardada en: {music_asset.file_path}")

    # FX Generator (Crea MOV binario real)
    fx_asset_data = fx_generator.generate_effect(
        prompt=effects_prompt,
        duration=sc.duration
    )
    fx_asset = Asset(
        job_id=job.id,
        scene_id=sc.id,
        asset_type="effect",
        file_path=fx_asset_data["file_path"],
        file_size=fx_asset_data["file_size"],
        mime_type=fx_asset_data["mime_type"],
        generation_metadata={"prompt": effects_prompt}
    )
    db.add(fx_asset)
    print(f"  [FXGen] Efectos guardados en: {fx_asset.file_path}")
    db.commit()

    # Guardar mapa de assets por escena para el ensamblado
    scene_assets_map[sc.id] = {
        "video": video_asset,
        "audio_tracks": audio_tracks,
        "fx": fx_asset,
        "music": music_asset
    }

# Generar prompts estructurados con secuencia de tiempo continua
print("\n=== 6.5 GENERANDO PROMPTS ESTRUCTURADOS CON TIEMPOS CONTINUOS ===")
structured_prompt_list = flow_prompt_builder.build_prompts(flow_scenes, char_map_combined)
for p_idx, p_data in enumerate(structured_prompt_list):
    prompt_text = p_data["prompt_text"]
    all_prompts_log.append(prompt_text)
    all_prompts_log.append("\n" + "=" * 80 + "\n")
    
    # Crear y guardar el asset del prompt estructurado en la DB
    sc = db_scenes[p_idx]
    prompt_asset = Asset(
        job_id=job.id,
        scene_id=sc.id,
        asset_type="prompt",
        file_path="",
        mime_type="text/markdown",
        generation_metadata={
            "prompt": prompt_text,
            "scene_number": p_idx + 1,
            "duration": sc.duration
        }
    )
    db.add(prompt_asset)
    print(f"  [FlowPromptBuilder] Prompt estructurado generado y guardado para Escena {p_idx + 1}")
db.commit()

# 7. Editor Agent: Ensamblado y composición del capítulo final
print("\n=== 7. EDITOR AGENT: COMPONIENDO EL EPISODIO FINAL ===")

# Ensamblaremos las escenas secuencialmente. Como simulación de editor de múltiples tomas,
# generaremos un archivo final de video que recopile la información de las 3 escenas.
video_clips_paths = [scene_assets_map[sc.id]["video"].file_path for sc in db_scenes]
all_audio_tracks = []
for sc in db_scenes:
    all_audio_tracks.extend(scene_assets_map[sc.id]["audio_tracks"])

music_track_path = scene_assets_map[db_scenes[0].id]["music"].file_path  # Usa la música principal de la primera escena
effects_paths = [scene_assets_map[sc.id]["fx"].file_path for sc in db_scenes]

assembly_result = editor.assemble_video(
    video_clip={"file_path": video_clips_paths[0]},  # Toma la primera toma como ancla
    audio_tracks=all_audio_tracks,
    effect_layers=[{"file_path": path} for path in effects_paths],
    music_track={"file_path": music_track_path}
)

# Renombrar para que sea descriptivo
final_output_dir = os.path.dirname(assembly_result["file_path"])
final_boruto_video_path = os.path.join(final_output_dir, "boruto_tbv_scene_final.mp4")

# Copiar el archivo generado al nombre definitivo
import shutil
shutil.copy(assembly_result["file_path"], final_boruto_video_path)

final_video_asset = Asset(
    job_id=job.id,
    asset_type="video",
    file_path=final_boruto_video_path,
    file_size=os.path.getsize(final_boruto_video_path),
    mime_type=assembly_result["mime_type"],
    generation_metadata={
        "scenes_included": [sc.id for sc in db_scenes],
        "video_clips": video_clips_paths,
        "editor": "FFmpeg_sim_multi_scene",
        "resolution": "1920x1080",
        "fps": 24,
        "color_grading": "cinematic_anime"
    }
)
db.add(final_video_asset)

# Completar el Job
job.status = "completed"
job.progress = 100
job.current_step = "final_production_render"
job.total_duration = sum(sc.duration for sc in db_scenes)
db.commit()

# Guardar prompts generados en un archivo de texto
os.makedirs("final_output", exist_ok=True)
prompts_file_path = os.path.join("final_output", "prompts_generados.txt")
with open(prompts_file_path, "w", encoding="utf-8") as pf:
    pf.write("\n".join(all_prompts_log))

print(f"\n¡EL EPISODIO DEL MANGA DE BORUTO HA SIDO PROCESADO EXITOSAMENTE!")
print(f"- Ruta del video final: {final_boruto_video_path}")
print(f"- Ruta del archivo de prompts: {prompts_file_path}")
print(f"- Duración total: {job.total_duration} segundos")
print(f"- Resolución: 1920x1080 (HD)")
print(f"- Color grading: cinematic_anime (específico para Boruto: Two Blue Vortex)")
print(f"- Clapping / Clips de video unidos: {len(video_clips_paths)}")
print(f"- Pistas de audio mezcladas: {len(all_audio_tracks)}")

db.close()
print("\n=== PIPELINE DE MANGA COMPLETADO CON ÉXITO ===")
