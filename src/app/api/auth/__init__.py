from flask import Blueprint, request
from config import *
from lib import jsonify
from app.models.users import Users

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/token', methods=['POST'])
def generateUserToken():
    data = request.get_json()
    res = Users.generateToken(data)
    if not res:
        return jsonify({'status': 'error', 'message': 'Unable to send token'}), 400
    return jsonify({'status': 'success', 'message': 'Verify using the otp sent to your email'}), 200

@auth.route('/verify', methods=['POST'])
def verifyUserToken():
    data = request.get_json()
    verified = Users.verify(data["email"], data["token"], data["username"])
    if not verified:
        return jsonify({'status': 'error', 'message': 'Unable to verify user'}), 400
    
    existing = Users.findByUID(f"{data['username']}@{Config.HOST}")
    if existing:
        return jsonify({'status': 'success', 'auth_token': '<send_auth_token>'}), 200
    else:
        userId = Users.add({
            "uid": f"{data['username']}@{Config.HOST}",
            "email": data["email"],
            "username": data["username"],
        })
        return jsonify({'status': 'success', 'created': userId, 'auth_token': '<send_auth_token>'}), 200
