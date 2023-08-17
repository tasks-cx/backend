from functools import wraps
from flask import g, session, make_response

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return make_response('Unauthorized', 401)
        return f(*args, **kwargs)
    return decorated_function


def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']
