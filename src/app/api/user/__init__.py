from flask import Blueprint, request
from config import *
from lib import jsonify
from lib.security import authorized
from app.models.users import Users

API_BASE = "/api/v" + Config.API_VERSION
users = Blueprint('users', __name__, url_prefix=API_BASE + '/users')

@users.route('/<id>', methods=['GET'])
@authorized
def userDetail(id):
    user = Users.findByUID(id)
    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 400
    return jsonify({'status': 'success', 'user': user }), 200
