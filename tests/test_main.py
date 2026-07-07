def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Live Action Studio" in response.text

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}