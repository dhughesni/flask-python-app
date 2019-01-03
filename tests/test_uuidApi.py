import pytest, urllib2
from flask import url_for

def test_getUUID(client, unitRemote):
    api = "/api/v0/uuid/"
    if unitRemote == None:
        assert client.get(api).status_code == 200
    elif unitRemote != None:
        assert urllib2.urlopen(unitRemote + api).code == 200

def test_checkUUID(client, unitRemote):
    api = "/api/v0/uuid/123"
    if unitRemote == None:
        assert client.get(api).status_code == 200
    elif unitRemote != None:
        assert urllib2.urlopen(unitRemote + api).code == 200
