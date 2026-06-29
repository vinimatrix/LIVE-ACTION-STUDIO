import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.agents.character_manager.character_manager import CharacterManagerAgent

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_cm.db"


@pytest.fixture
def db_session():
    from app.models import Character
    engine = create_engine(
        SQLALCHEMY_TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal


def test_character_manager_initialization(db_session):
    agent = CharacterManagerAgent(db_session=db_session)
    assert agent is not None


def test_get_or_create_character(db_session):
    agent = CharacterManagerAgent(db_session=db_session)
    result = agent.get_or_create_character("Hero", ["brave", "strong"])
    assert result["name"] == "Hero"
    assert result["personality_traits"] == ["brave", "strong"]


def test_process_screenplay(db_session):
    agent = CharacterManagerAgent(db_session=db_session)
    screenplay_data = {
        "scene_id": 1,
        "dialogue": [
            {"character": "Hero", "text": "I will win!", "emotion": "determined"},
            {"character": "Villain", "text": "Never!", "emotion": "angry"}
        ],
        "actions": ["Hero prepares to fight"]
    }

    result = agent.process_screenplay(screenplay_data)

    assert "character_data" in result
    assert "Hero" in result["character_data"]
    assert "Villain" in result["character_data"]
    assert result["character_data"]["Hero"]["name"] == "Hero"
