from app.api.auth import auth
from app.api.user import users
from app.api.projects import projects
from app.api.tasks import tasks

def register_apis(app):
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(tasks)
