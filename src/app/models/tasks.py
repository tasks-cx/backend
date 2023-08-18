from app.models import db

class Tasks:

    def add(self, data):
        task_id = db.tasks.insert_one(data).inserted_id
        return None if not task_id else task_id
    
    def list(project_id):
        tasks = db.tasks.find({
            'project_id': project_id
        }).limit(100)
        return [t for t in tasks]