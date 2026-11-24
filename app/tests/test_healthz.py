from fastapi.testclient import TestClient

from uptime_monitor.api.app import create_app

client = TestClient(create_app())


def test_health_check():
    resp = client.get("/healthz")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
