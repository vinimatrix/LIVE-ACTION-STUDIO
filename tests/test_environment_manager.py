import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.agents.environment_manager.environment_manager import EnvironmentManagerAgent

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_em.db"


@pytest.fixture
def db_session():
    from app.models import Environment
    engine = create_engine(
        SQLALCHEMY_TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal


def test_environment_manager_initialization(db_session):
    agent = EnvironmentManagerAgent(db_session=db_session)
    assert agent is not None


def test_get_or_create_environment(db_session):
    agent = EnvironmentManagerAgent(db_session=db_session)
    result = agent.get_or_create_environment("forest", "Enchanted Forest")

    assert result["name"] == "Enchanted Forest"
    assert result["location_type"] == "forest"


def test_process_screenplay(db_session):
    agent = EnvironmentManagerAgent(db_session=db_session)
    screenplay_data = {
        "scene_id": 1,
        "description": "A dark forest scene",
        "dialogue": [],
        "actions": ["Character walks through forest"],
        "duration": 5.0
    }

    result = agent.process_screenplay(screenplay_data)

    assert "environment_data" in result
    assert result["environment_data"]["name"] == "Default Interior"
    assert result["environment_data"]["location_type"] == "interior"
