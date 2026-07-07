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


class TestDirectorAgent:
    def test_process_manga_request_passes_director_style(self, db_session, mocker):
        agent = DirectorAgent(db_session=db_session)

        mock_analyze = mocker.patch.object(agent, 'manga_analyzer')
        mock_analyze.analyze.return_value = {
            "characters": [], "setting": "test", "action": "",
            "dialogue": [], "mood": ""
        }

        mock_compose = mocker.patch.object(agent, 'scene_composer')
        mock_compose.compose.return_value = [{
            "scene_id": 1, "duration": 8.0, "characters": [],
            "description": "test", "camera": {}, "lighting": {},
            "dialogue": [], "transition": "cut"
        }]

        mock_prompt = mocker.patch.object(agent, 'prompt_builder')
        mock_prompt.build_prompts.return_value = [{
            "scene_id": 1, "scene_number": 1, "duration": 8.0,
            "prompt_text": "test prompt"
        }]

        agent.process_manga_request({
            "image": "fake_base64",
            "filename": "test.png",
            "character_mapping": {"Goku": "personaje_1"},
            "options": {"director_style": "michael_bay"}
        })

        mock_compose.compose.assert_called_once()
        _, kwargs = mock_compose.compose.call_args
        assert kwargs.get("director_style") == "michael_bay"

        mock_prompt.build_prompts.assert_called_once()
        _, kwargs = mock_prompt.build_prompts.call_args
        assert kwargs.get("director_style") == "michael_bay"


    def test_director_initialization(self, db_session):
        agent = DirectorAgent(db_session=db_session)
        assert agent is not None
        assert hasattr(agent, 'settings')

    def test_process_manga_request_creates_job(self, db_session, mocker):
        agent = DirectorAgent(db_session=db_session)

        mock_analyze = mocker.patch.object(agent, 'manga_analyzer')
        mock_analyze.analyze.return_value = {
            "characters": [], "setting": "test", "action": "",
            "dialogue": [], "mood": ""
        }

        mock_compose = mocker.patch.object(agent, 'scene_composer')
        mock_compose.compose.return_value = [{
            "scene_id": 1, "duration": 8.0, "characters": [],
            "description": "test", "camera": {}, "lighting": {},
            "dialogue": [], "transition": "cut"
        }]

        mock_prompt = mocker.patch.object(agent, 'prompt_builder')
        mock_prompt.build_prompts.return_value = [{
            "scene_id": 1, "scene_number": 1, "duration": 8.0,
            "prompt_text": "test prompt"
        }]

        job_id = agent.process_manga_request({
            "filename": "test.png",
            "image": "base64data",
            "character_mapping": {"Goku": "personaje_1"},
            "options": {"max_scenes": 3}
        })

        assert isinstance(job_id, int)
        assert job_id > 0

        db = db_session()
        from app.models import Job, Scene, Asset
        job = db.query(Job).filter(Job.id == job_id).first()
        assert job is not None
        assert job.status == "completed"
        assert job.manga_filename == "test.png"

        scenes = db.query(Scene).filter(Scene.job_id == job_id).all()
        assert len(scenes) == 1

        assets = db.query(Asset).filter(Asset.job_id == job_id).all()
        assert len(assets) == 1
        assert assets[0].asset_type.value == "prompt"
        db.close()

    def test_get_next_task(self, db_session, mocker):
        agent = DirectorAgent(db_session=db_session)

        mock_analyze = mocker.patch.object(agent, 'manga_analyzer')
        mock_analyze.analyze.return_value = {
            "characters": [], "setting": "test", "action": "",
            "dialogue": [], "mood": ""
        }

        mock_compose = mocker.patch.object(agent, 'scene_composer')
        mock_compose.compose.return_value = [{
            "scene_id": 1, "duration": 8.0, "characters": [],
            "description": "test", "camera": {}, "lighting": {},
            "dialogue": [], "transition": "cut"
        }]

        mock_prompt = mocker.patch.object(agent, 'prompt_builder')
        mock_prompt.build_prompts.return_value = [{
            "scene_id": 1, "scene_number": 1, "duration": 8.0,
            "prompt_text": "test prompt"
        }]

        job_id = agent.process_manga_request({
            "filename": "test.png",
            "image": "base64data",
            "character_mapping": {},
            "options": {}
        })

        task = agent.get_next_task(job_id)
        assert task["job_id"] == job_id
        assert task["task_type"] == "completed"
        assert task["status"] == "completed"

    def test_get_next_task_not_found(self, db_session):
        agent = DirectorAgent(db_session=db_session)
        task = agent.get_next_task(9999)
        assert task == {"error": "Job not found"}
