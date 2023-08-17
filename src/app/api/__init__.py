from app.api.projects import projects
from app.api.user import users

def register_apis(app):
    app.register_blueprint(users)
    app.register_blueprint(projects)
