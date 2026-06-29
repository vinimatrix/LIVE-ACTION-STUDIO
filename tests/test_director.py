import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.agents.director.director import DirectorAgent

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_director.db"


@pytest.fixture
def db_session():
    from app.models import Character, Environment, Scene, SceneCharacter, Asset, Job
    engine = create_engine(
        SQLALCHEMY_TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    db.add(Environment(
        name="Default",
        description="Default test environment",
        location_type="interior",
        visual_references=[],
        lighting_conditions={},
        props=[]
    ))
    db.commit()
    db.close()

    yield TestingSessionLocal


def test_director_initialization(db_session):
    agent = DirectorAgent(db_session=db_session)
    assert agent is not None
    assert hasattr(agent, 'settings')


def test_process_manga_request(db_session):
    agent = DirectorAgent(db_session=db_session)
    manga_data = {
        "filename": "test_manga.jpg",
        "page_url": "http://example.com/page1.jpg"
    }
    job_id = agent.process_manga_request(manga_data)
    assert isinstance(job_id, int)
    assert job_id > 0


def test_get_next_task(db_session):
    agent = DirectorAgent(db_session=db_session)
    manga_data = {
        "filename": "test_manga.jpg",
        "page_url": "http://example.com/page1.jpg"
    }
    job_id = agent.process_manga_request(manga_data)
    task = agent.get_next_task(job_id)
    assert task["job_id"] == job_id
    assert task["task_type"] == "process_scene"
    assert task["data"]["scene_id"] is not None
