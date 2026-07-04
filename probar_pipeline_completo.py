import os
import sys
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
from app.agents.image_generator.image_generator import ImageGeneratorAgent
from app.agents.video_generator.video_generator import VideoGeneratorAgent
from app.agents.voice_generator.voice_generator import VoiceGeneratorAgent
from app.agents.music_generator.music_generator import MusicGeneratorAgent
from app.agents.fx_generator.fx_generator import FXGeneratorAgent
from app.agents.editor.editor import EditorAgent

# 1. Configurar base de datos SQLite para la prueba del pipeline completo
print("=== 1. CONFIGURANDO BASE DE DATOS DE PRUEBA ===")
DB_URL = "sqlite:///./prueba_pipeline_completo.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Limpiar ejecuciones anteriores de la base de datos
db = SessionLocal()
db.query(Asset).delete()
db.query(Scene).delete()
db.query(Job).delete()
db.query(Character).delete()
db.query(Environment).delete()
db.commit()

# 2. Inicializar los agentes con la sesión de base de datos correspondiente
print("=== 2. INICIALIZANDO AGENTES ===")
director = DirectorAgent(db_session=SessionLocal)
screenwriter = ScreenwriterAgent()
character_manager = CharacterManagerAgent(db_session=SessionLocal)
environment_manager = EnvironmentManagerAgent(db_session=SessionLocal)
prompt_builder = PromptBuilderAgent()
image_generator = ImageGeneratorAgent()
video_generator = VideoGeneratorAgent()
voice_generator = VoiceGeneratorAgent()
music_generator = MusicGeneratorAgent()
fx_generator = FXGeneratorAgent()
editor = EditorAgent()

print("Agentes inicializados exitosamente.")

# 3. Registrar Entorno y Personaje de referencia en la base de datos (Biblia del Universo)
print("\n=== 3. REGISTRANDO LA BIBLIA DEL UNIVERSO (Solo Leveling) ===")
# Registrar personaje: Sung Jinwoo
jinwoo = character_manager.get_or_create_character(
    character_name="Sung Jinwoo",
    traits=["Valiente", "Silencioso", "Poderoso", "Mirada intensa"],
)
# Actualizar datos de Jinwoo con referencias visuales y voz
db_jinwoo = db.query(Character).filter(Character.id == jinwoo["id"]).first()
db_jinwoo.visual_references = ["/assets/references/jinwoo_face.jpg"]
db_jinwoo.expressions = ["determinado", "serio", "monarca"]
db_jinwoo.outfits = [{"name": "hunter_armor", "ref": "/assets/references/jinwoo_armor.jpg"}]
db_jinwoo.voice_profile = "eleven_labs_jinwoo_voice_id"
db.commit()
print(f"Personaje registrado: {db_jinwoo.name} (ID: {db_jinwoo.id})")

# Registrar entorno: Dungeon Oscuro
dungeon = Environment(
    name="Dungeon Oscuro",
    description="Un calabozo subterráneo oscuro lleno de runas brillantes y niebla volumétrica",
    location_type="dungeon",
    visual_references=["/assets/references/dungeon_bg.jpg"],
    lighting_conditions={"time_of_day": "night", "weather": "foggy", "style": "dark_fantasy"},
    props=["rife gates", "altars", "glowing runes"]
)
db.add(dungeon)
db.commit()
print(f"Entorno registrado: {dungeon.name} (ID: {dungeon.id})")

# 4. Iniciar el Pipeline: Procesar una página de manga
print("\n=== 4. DIRECTOR AGENT: PROCESANDO PÁGINA DE MANGA ===")
manga_request = {
    "filename": "solo_leveling_ch1_p5.jpg",
    "page_url": "http://manga-reader.local/solo_leveling/ch1/p5.jpg"
}
job_id = director.process_manga_request(manga_request)
job = db.query(Job).filter(Job.id == job_id).first()
scene = db.query(Scene).filter(Scene.job_id == job_id).first()
print(f"Job creado. ID: {job.id}, Status: {job.status}")
print(f"Scene creada. ID: {scene.id}, Referencia Manga: {scene.manga_page_reference}")

# 5. Screenwriter Agent: Procesar la escena y generar el guión cinematográfico
print("\n=== 5. SCREENWRITER AGENT: GENERANDO GUION CINEMATOGRÁFICO ===")
screenplay_input = {
    "scene_id": scene.id,
    "dialogue": [
        {"character": "Sung Jinwoo", "text": "No puedo morir aquí... no todavía.", "emotion": "determinado"}
    ],
    "actions": ["Sung Jinwoo aprieta su daga.", "Las runas del calabozo brillan intensamente."]
}
screenplay_result = screenwriter.process_scene(screenplay_input)
print("Guión generado exitosamente:")
print(f"- Diálogos: {screenplay_result.get('dialogue')}")
print(f"- Acciones: {screenplay_result.get('actions')}")

# 6. Character & Environment Managers: Vincular datos a la escena
print("\n=== 6. MANAGERS DE CONSISTENCIA: CARGANDO REFERENCIAS ===")
# Asociar personaje y entorno a la escena en DB
scene.environment_id = dungeon.id
db.commit()

# Procesar los personajes participantes de la escena
char_data_processed = character_manager.process_screenplay(screenplay_result)
print(f"Personajes vinculados y verificados: {list(char_data_processed.get('character_data', {}).keys())}")

# Obtener datos completos de la escena para construir prompts
scene_full_data = {
    "description": scene.description + " - " + " ".join(screenplay_result["actions"]),
    "duration": scene.duration,
    "character_data": char_data_processed.get("character_data", {}),
    "environment_data": {
        "location_type": dungeon.location_type,
        "lighting_conditions": dungeon.lighting_conditions
    },
    "camera_notes": {
        "shot_type": "close-up",
        "movement": "slow dolly forward"
    }
}

# 7. Prompt Builder Agent: Construir prompts específicos para cada IA
print("\n=== 7. PROMPT BUILDER AGENT: CONSTRUYENDO PROMPTS DE GENERACIÓN ===")
image_prompt = prompt_builder.build_image_prompt(scene_full_data)
video_prompt = prompt_builder.build_video_prompt(image_prompt, scene_full_data["duration"])
voice_prompts = [
    prompt_builder.build_voice_prompt(dial) for dial in screenplay_result["dialogue"]
]
music_prompt = prompt_builder.build_music_prompt(scene_full_data)
effects_prompt = prompt_builder.build_effects_prompt(screenplay_result)

print(f"- Prompt de Imagen: {image_prompt}\n")
print(f"- Prompt de Video: {video_prompt}\n")
print(f"- Prompt de Voz: {voice_prompts}\n")
print(f"- Prompt de Música: {music_prompt}\n")
print(f"- Prompt de FX: {effects_prompt}\n")

# 8. Generation Agents: Generar los assets correspondientes (Imágenes, Videos, Voz, Música, FX)
print("\n=== 8. GENERATION AGENTS: CREANDO ASSETS MULTIMEDIA ===")

# Generación de Imagen (con fallback si no hay ComfyUI)
image_asset_data = image_generator.generate_image(image_prompt, scene_id=scene.id)
image_asset = Asset(
    job_id=job.id,
    scene_id=scene.id,
    asset_type="image",
    file_path=image_asset_data["file_path"],
    file_size=image_asset_data["file_size"],
    mime_type=image_asset_data["mime_type"],
    generation_metadata=image_asset_data["generation_params"]
)
db.add(image_asset)
print(f"Asset Imagen generado: {image_asset.file_path} ({image_asset_data['generation_params']['model']})")

# Generación de Video (animando la imagen)
video_asset_data = video_generator.generate_video(
    image_path=image_asset.file_path,
    prompt=video_prompt,
    duration=scene.duration
)
video_asset = Asset(
    job_id=job.id,
    scene_id=scene.id,
    asset_type="video",
    file_path=video_asset_data["file_path"],
    file_size=video_asset_data["file_size"],
    mime_type=video_asset_data["mime_type"],
    generation_metadata=video_asset_data["generation_params"]
)
db.add(video_asset)
print(f"Asset Video generado: {video_asset.file_path} ({video_asset_data['generation_params']['model']})")

# Generación de Voces
audio_tracks = []
for idx, voice_pr in enumerate(voice_prompts):
    voice_asset_data = voice_generator.generate_voice(
        prompt=voice_pr,
        character_id=db_jinwoo.id
    )
    voice_asset = Asset(
        job_id=job.id,
        scene_id=scene.id,
        asset_type="audio",
        file_path=voice_asset_data["file_path"],
        file_size=voice_asset_data["file_size"],
        mime_type=voice_asset_data["mime_type"],
        generation_metadata={"prompt": voice_pr}
    )
    db.add(voice_asset)
    audio_tracks.append({"file_path": voice_asset.file_path})
    print(f"Asset Voz [{idx}] generado: {voice_asset.file_path}")

# Generación de Música
music_asset_data = music_generator.generate_music(
    prompt=music_prompt,
    duration=scene.duration
)
music_asset = Asset(
    job_id=job.id,
    scene_id=scene.id,
    asset_type="music",
    file_path=music_asset_data["file_path"],
    file_size=music_asset_data["file_size"],
    mime_type=music_asset_data["mime_type"],
    generation_metadata={"prompt": music_prompt}
)
db.add(music_asset)
print(f"Asset Música generado: {music_asset.file_path}")

# Generación de FX Visuales/Sonoros
fx_asset_data = fx_generator.generate_effect(
    prompt=effects_prompt,
    duration=scene.duration
)
fx_asset = Asset(
    job_id=job.id,
    scene_id=scene.id,
    asset_type="effect",
    file_path=fx_asset_data["file_path"],
    file_size=fx_asset_data["file_size"],
    mime_type=fx_asset_data["mime_type"],
    generation_metadata={"prompt": effects_prompt}
)
db.add(fx_asset)
print(f"Asset FX generado: {fx_asset.file_path}")
db.commit()

# 9. Editor Agent: Ensamblar los elementos en el clip final
print("\n=== 9. EDITOR AGENT: ENSAMBLANDO EPISODIO FINAL ===")
assembly_result = editor.assemble_video(
    video_clip={"file_path": video_asset.file_path},
    audio_tracks=audio_tracks,
    effect_layers=[{"file_path": fx_asset.file_path}],
    music_track={"file_path": music_asset.file_path}
)

final_video_asset = Asset(
    job_id=job.id,
    asset_type="video",
    file_path=assembly_result["file_path"],
    file_size=assembly_result["file_size"],
    mime_type=assembly_result["mime_type"],
    generation_metadata=assembly_result["generation_params"]
)
db.add(final_video_asset)

# Actualizar estado del Job a completado
job.status = "completed"
job.progress = 100
job.current_step = "final_assembly"
job.total_duration = scene.duration
db.commit()

print(f"¡EPISODIO ENSAMBLADO EXITOSAMENTE!")
print(f"- Ruta del video final: {assembly_result['file_path']}")
print(f"- Resolución: {assembly_result['generation_params']['resolution']}")
print(f"- FPS: {assembly_result['generation_params']['fps']}")
print(f"- Color grading: {assembly_result['generation_params']['color_grading']}")

# Cerrar sesión de base de datos
db.close()
print("\n=== PRUEBA DE PIPELINE TERMINADA CON ÉXITO ===")
