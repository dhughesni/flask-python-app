import pytest

def test_checkStatus(client):
    rep = client.get("/")
    assert rep.status_code == 200
