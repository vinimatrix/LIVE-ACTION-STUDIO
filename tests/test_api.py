import os
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.db import session as db_session_module

TEST_DATABASE_URL = "sqlite:///./test_api.db"


@pytest.fixture(scope="module")
def engine():
    eng = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    yield eng
    eng.dispose()


@pytest.fixture(scope="module")
def test_db(engine):
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )

    from app.models import Environment
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    session.add(Environment(
        name="Default",
        description="Default test environment",
        location_type="interior",
        visual_references=[],
        lighting_conditions={},
        props=[]
    ))
    session.commit()
    session.close()

    original = db_session_module.SessionLocal
    db_session_module.SessionLocal = TestingSessionLocal
    yield
    db_session_module.SessionLocal = original
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client, test_db):
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Live Action Studio" in response.text


def test_health_endpoint(client, test_db):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@patch("app.api.v1.endpoints.manga.DirectorAgent")
def test_process_manga_endpoint(mock_director, client, test_db):
    mock_director.return_value.process_manga_request.return_value = 42
    response = client.post("/api/v1/manga/process", json={
        "filename": "test_manga.jpg",
        "page_url": "http://example.com/page1.jpg"
    })
    assert response.status_code == 202
    data = response.json()
    assert data["message"] == "Processing started"
    assert data["filename"] == "test_manga.jpg"
    assert data["status"] == "accepted"


def test_get_job_status_not_found(client, test_db):
    response = client.get("/api/v1/jobs/status/99999")
    assert response.status_code == 404


@patch("app.api.v1.endpoints.manga.FlowPromptBuilderAgent")
@patch("app.api.v1.endpoints.manga._get_session")
@patch("app.api.v1.endpoints.manga.DirectorAgent")
def test_upload_endpoint(mock_director, mock_session, mock_flow, client, test_db):
    from unittest.mock import MagicMock
    mock_job = MagicMock()
    mock_job.id = 42
    mock_job.manga_filename = "test.png"
    mock_job.status = "completed"
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.order_by.return_value.all.return_value = []
    mock_db.query.return_value.filter.return_value.all.return_value = []
    mock_db.query.return_value.filter.return_value.first.return_value = mock_job
    mock_session.return_value = mock_db
    mock_director.return_value.process_manga_request.return_value = 42

    png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
    response = client.post("/api/v1/manga/upload", files={"file": ("test.png", png, "image/png")})
    assert response.status_code == 200
    data = response.json()
    assert data["job_id"] == 42
    assert data["filename"] == "test.png"
