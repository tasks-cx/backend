from config import *
from flask import Flask

from lib.security import before_request

# Import blueprint(s)
from app.api import register_apis
from app.jobs import create_celery
from app.views import register_views

# Check Celery config
if not CeleryConf.BROKER_URL:
    exit('config BROKER_URL missing')

# Initialize DB by providing app context
# def init_db(app):
#    db.init_app(app)

# Create a flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Setup some secret
    # app.secret_key = Config.SECRET_KEY

    # Initialize DB
    # init_db(app)

    # Initialize Celery provider
    create_celery(app)

    # Set pre request
    app.before_request(before_request)

    # Register blueprints
    register_views(app)
    register_apis(app)

    return app
