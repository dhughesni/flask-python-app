from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from . import log
from . import uuidApi
LOG = log.setup_custom_logger('root')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# create_app wrapps the other functions to set up the project
def create_app(config=None, testing=False, cli=True):
    """
    Application factory, used to create application
    """
    app = Flask(__name__, static_folder=None)

    # configure_app(app, testing)
    # configure_extensions(app, cli)
    register_blueprints(app)

    # status check
    @app.route('/')
    def checkStatus():
        return 'App is running!'

    LOG.info('App Started!')
    # return from create_app
    return app

def register_blueprints(app):
    """
    register all blueprints for application
    """
    app.register_blueprint(uuidApi.views.blueprint)
