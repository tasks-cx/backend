import crypt
from config import Config
from functools import wraps
from flask import g, request, redirect, url_for, session, make_response

def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('home_view.login', _external=True, _scheme='https', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']
