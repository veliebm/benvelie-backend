import app
import pytest


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_home_route_tells_user_off(client):
    return_value = client.get("/ping")

    assert b"pong" in return_value.data
