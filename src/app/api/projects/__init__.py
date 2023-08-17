from flask import Blueprint, request
from config import *
from lib import jsonify
from lib.security import authorized

API_BASE = "/api/v" + Config.API_VERSION
projects = Blueprint('projects', __name__, url_prefix=API_BASE + '/projects')

@projects.route('', methods=['POST'])
@authorized
def createProject():
    data = request.get_json()
    return jsonify({'status': 'success', 'project': data }), 200

@projects.route('/<id>', methods=['GET'])
@authorized
def projectDetail(id):
    return jsonify({'status': 'success', 'project': id }), 200
