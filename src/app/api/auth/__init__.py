from flask import Blueprint, request, session
from config import *
from lib import jsonify
from app.models.users import Users
from jwt import encode

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
    uid = f"{data['username']}@{Config.HOST}"
    verified = Users.verify(data["email"], data["token"])
    if not verified:
        return jsonify({'status': 'error', 'message': 'Unable to verify user'}), 400
    
    existing = Users.findByUID(uid)
    if existing:
        session['user'] = str(existing["uid"])
        payload_data = {
            "sub": str(existing["uid"])
        }
        auth_token = encode(payload_data, Config.SESSION_SECRET, algorithm='HS256')
        return jsonify({'status': 'success', 'auth_token': auth_token }), 200
    else:
        userId = Users.add({
            "uid": uid,
            "email": data["email"],
            "username": data["username"],
        })
        session['user'] = str(userId)
        payload_data = {
            "sub": str(userId)
        }
        auth_token = encode(payload_data, Config.SESSION_SECRET, algorithm='HS256')
        return jsonify({'status': 'success', 'created': userId, 'auth_token': auth_token}), 200
