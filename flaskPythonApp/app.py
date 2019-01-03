from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from . import uuidApi
from . import log
LOG = log.setup_custom_logger('root')

# create_app wrapps the other functions to set up the project
def create_app(config=None, testing=False, cli=True):
    """
    Application factory, used to create application
    """
    app = Flask(__name__, static_folder=None)
    register_blueprints(app)

    # status check
    @app.route('/')
    def checkStatus():
        return 'App is running!'

    LOG.info('App Started!')
    return app

def register_blueprints(app):
    """
    register all blueprints for application
    """
    app.register_blueprint(uuidApi.views.blueprint)
