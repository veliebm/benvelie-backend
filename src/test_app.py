import json
import app
import pytest
from app import app, Totals, MAX_CLICK_RATE, database


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            database.create_all()
            totals_already_exist = (
                database.session.query(Totals).filter(Totals.id == 1).first()
            )
            if not totals_already_exist:
                database.session.add(Totals(id=1, click_count=0, observation_time=0))
                database.session.commit()
            yield client


def test_home_route_tells_user_off(client):
    rv = client.get("/")
    assert b"seeing" in rv.data


def test_get_totals_observation_time_should_increment_by_one_each_request(client):
    rv1 = client.get("/totals?click_count=0")
    rv2 = client.get("/totals?click_count=0")
    data1 = json.loads(rv1.data)
    data2 = json.loads(rv2.data)
    assert data2["observation_time"] - data1["observation_time"] == 1


def test_get_totals_click_count_should_not_be_negative(client):
    rv = client.get("/totals?click_count=-5")
    assert b"less than 0" in rv.data
    assert rv.status_code == 400


def test_get_totals_click_count_should_truncate_to_max_click_rate(client):
    start_click_count = int(
        json.loads(client.get("/totals?click_count=0").data)["click_count"]
    )
    rv = client.get(f"/totals?click_count={MAX_CLICK_RATE + 10}")
    data = json.loads(rv.data)
    assert data["click_count"] == start_click_count + MAX_CLICK_RATE