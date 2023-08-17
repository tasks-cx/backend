from flask import Blueprint, request
from config import *
from lib import jsonify
from lib.security import authorized

API_BASE = "/api/v" + Config.API_VERSION
users = Blueprint('users', __name__, url_prefix=API_BASE + '/users')

@users.route('', methods=['POST'])
def createUser():
    data = request.get_json()
    return jsonify({'status': 'success', 'user': data }), 200

@users.route('/<id>', methods=['GET'])
@authorized
def userDetail(id):
    return jsonify({'status': 'success', 'user': id }), 200
