import pytest
from flaskPythonApp.app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app

def pytest_addoption(parser):
    parser.addoption("--unitRemote", action="store", default=None, help="run unit tests against remote server")

@pytest.fixture
def unitRemote(request):
    return request.config.getoption("--unitRemote")
