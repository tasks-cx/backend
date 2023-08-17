from app.models import db

class Users:
    def add(data):
        user_id = db.users.insert_one(data).inserted_id
        return None if not user_id else user_id
    
    def list():
        users = db.users.find()
        return [u for u in users]