from flask_restful import Resource
from flask import jsonify
import logging, uuid
LOG = logging.getLogger('root')

class getUUID(Resource):
    def get(self):
        """
        Make a UUID based on the host ID and current time
        """
        return jsonify({'UUID': uuid.uuid1()})

class checkUUID(Resource):
    def get(self, uuid_string):
        """
        Check if UUID is valid
        """
        try:
            val = uuid.UUID(uuid_string)
        except ValueError:
            LOG.info('validateUUID Results: UUID:' + uuid_string + ' = VALID: False')
            return jsonify({'UUID': uuid_string, 'VALID': False})
        LOG.info('validateUUID Results: UUID:' + uuid_string + ' = VALID:' + str(str(val) == uuid_string))
        return jsonify({'UUID': uuid_string, 'VALID': str(val) == uuid_string})
