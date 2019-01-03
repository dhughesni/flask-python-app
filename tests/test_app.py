import pytest, urllib2
from flask import url_for

def test_checkStatus(client, unitRemote):
    api = "/"
    if unitRemote == None:
        assert client.get(api).status_code == 200
    elif unitRemote != None:
        assert urllib2.urlopen(unitRemote + api).code == 200        
