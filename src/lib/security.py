import crypt
from config import Config
from functools import wraps
from lib import jsonify
from flask import g, request, redirect, url_for, session
from jwt import decode, ExpiredSignatureError, InvalidTokenError

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check session from header
        if 'Authorization' in request.headers:
            auth = request.headers['Authorization'].split()
            if len(auth) == 2:
                if auth[0].lower() == 'bearer':
                    token = auth[1]
                    try:
                        payload = decode(token, Config.SESSION_SECRET, algorithms=['HS256'])
                        g.user = payload['sub']
                        return f(*args, **kwargs)
                    except ExpiredSignatureError:
                        return jsonify({'status': 'error', 'message': 'Expired token. Please log in again.'}), 401
                    except InvalidTokenError:
                        return jsonify({'status': 'error', 'message': 'Invalid token. Please log in again.'}), 401

        # Check session from cookie
        if g.user is None:
            return jsonify({'status': 'error', 'message': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']
