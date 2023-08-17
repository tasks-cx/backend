from flask import Blueprint, request
from config import *
from lib import jsonify
from lib.security import authorized
# from app.jobs.send_email import send_user_confirmation
from app.models.tasks import Tasks

API_BASE = "/api/v" + Config.API_VERSION
tasks = Blueprint('tasks', __name__, url_prefix=API_BASE + '/tasks')

@tasks.route('', methods=['POST'])
@authorized
def createTask():
    data = request.get_json()
    task_id = Tasks.add(data)
    return jsonify({'status': 'success', 'task_id': task_id }), 200

@tasks.route('/', methods=['GET'])
def taskList():
    all_tasks = Tasks.list()
    return jsonify({'status': 'success', 'task': all_tasks }), 200

@tasks.route('/<id>', methods=['GET'])
@authorized
def taskDetail(id):
    return jsonify({'status': 'success', 'task': id }), 200
