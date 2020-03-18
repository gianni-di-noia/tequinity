"""Main tests module."""
import app


def test_home():
    """Test Home page"""
    app.APP.testing = True
    client = app.APP.test_client()

    req = client.get("/")
    assert req.status_code == 302

    req = client.get("/categories")
    assert req.status_code == 200

    req = client.get("/all")
    assert req.status_code == 200

    req = client.get("/today")
    assert req.status_code == 200
