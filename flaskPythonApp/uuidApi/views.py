from flask import Blueprint
from flask_restful import Api
# import the name of the funciton/class
from .resources import getUUID, checkUUID
# setup blueprint
blueprint = Blueprint('uuidApi', __name__, url_prefix='/api/v0/uuid')
uuid_bp = Api(blueprint)
# add function, routes to api blueprint
uuid_bp.add_resource(getUUID, '/')
uuid_bp.add_resource(checkUUID, '/<uuid_string>')
