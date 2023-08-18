from app.models import db

class Projects:
    def add(data):
        project_id = db.projects.insert_one(data).inserted_id
        return None if not project_id else project_id
    
    def list():
        projects = db.projects.find().limit(100)
        return [p for p in projects]

