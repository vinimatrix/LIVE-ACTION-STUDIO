from app.db.session import SessionLocal, engine, Base
from app.models import Character, Environment, Scene, Asset, Job

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

    # Create initial data if needed
    db = SessionLocal()
    try:
        # Example: create a default character if none exist
        if db.query(Character).count() == 0:
            default_char = Character(
                name="Default Character",
                description="A placeholder character",
                visual_references=[],
                personality_traits=["neutral"],
                expressions=["neutral"],
                outfits=[],
                weapons=[],
                abilities=[],
                voice_profile="default_voice"
            )
            db.add(default_char)
            db.commit()
    finally:
        db.close()