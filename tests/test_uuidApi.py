import pytest

def test_getUUID(client):
    assert client.get("/api/v0/uuid/").status_code == 200

def test_checkUUID(client):
    assert client.get("/api/v0/uuid/123").status_code == 200
