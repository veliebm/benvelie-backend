import app


def test_home_route_tells_user_off():
    assert "seeing" in app.home()