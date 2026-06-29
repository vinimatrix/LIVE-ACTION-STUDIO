import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.db.session import Base

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

def test_database_connection():
    engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        # Test that we can query
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
    finally:
        db.close()

def test_model_creation():
    from app.models.character import Character

    engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    try:
        char = Character(
            name="Test Character",
            description="A test character",
            visual_references=["http://example.com/ref1.jpg"],
            personality_traits=["brave", "determined"],
            expressions=["happy", "sad", "angry"],
            outfits=[{"name": "default", "reference": "http://example.com/outfit1.jpg"}],
            weapons=[{"name": "sword", "reference": "http://example.com/weapon1.jpg"}],
            abilities=[{"name": "fireball", "description": "Throws fireballs"}],
            voice_profile="voice_model_1"
        )
        db.add(char)
        db.commit()
        db.refresh(char)

        assert char.id is not None
        assert char.name == "Test Character"
        assert len(char.visual_references) == 1
    finally:
        db.close()