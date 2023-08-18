from flask import Blueprint, request
from config import *
from lib import jsonify
from lib.security import authorized
# from app.jobs.send_email import send_user_confirmation
from app.models.projects import Projects

API_BASE = "/api/v" + Config.API_VERSION
projects = Blueprint('projects', __name__, url_prefix=API_BASE + '/projects')

@projects.route('', methods=['POST'])
@authorized
def createProject():
    data = request.get_json()
    project_id = Projects.add(data)
    return jsonify({'status': 'success', 'project_id': project_id }), 200

@projects.route('/', methods=['GET'])
@authorized
def projectList():
    all_projects = Projects.list()
    # send_user_confirmation.delay(all_projects)
    return jsonify({'status': 'success', 'projects': all_projects }), 200

@projects.route('/<id>', methods=['GET'])
@authorized
def projectDetail(id):
    return jsonify({'status': 'success', 'project': id }), 200
