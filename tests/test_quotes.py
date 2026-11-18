from quotes.main import app

def test_home():
    assert app.test_client().get("/").status_code == 200

def test_quote():
    r = app.test_client().get("/quote")
    assert r.status_code == 200
    assert "quote" in r.get_json()