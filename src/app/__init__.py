from config import *
from flask import Flask

from lib.security import before_request

from app.models import db

# Import blueprint(s)
from app.api import register_apis
from app.jobs import celery_init_app
from app.views import register_views

# Create a flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Setup some secret
    # app.secret_key = Config.SECRET_KEY

    # Initialize Celery provider
    celery_init_app(app)

    # Set pre request
    app.before_request(before_request)

    # Register blueprints
    register_views(app)
    register_apis(app)

    return app
