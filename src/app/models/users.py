from app.utils.otp import generate_otp
from app.models import db
from config import *
from app.jobs.send_email import send_user_confirmation
from app.entities.primitives import UserId

class Users:

    def generateToken(data):
        email = data["email"]
        token = generate_otp()
        existing = db.userTokens.find_one({ "email": email })
        if existing is None:
            db.userTokens.insert_one({
                "email": email,
                "token": token
            })
            Users.send_token(dict(email = email, token = token))
            return True

        db.userTokens.update_one(
            { "_id": existing["_id"] }, 
            { "$set": { "token": token } }
        )
        Users.send_token(dict(email = email, token = token))
        return True

    def add(data):
        existing = db.users.find_one({ "email": data["email"] })
        if existing is not None:
            return False
        user_id = db.users.insert_one(data).inserted_id
        return None if not user_id else data['uid']
    
    def list():
        users = db.users.find().limit(100)
        return [u for u in users]
    
    def findByUID(uid):
        user = db.users.find_one({ "uid": uid })
        return user
    
    def verify(email, token, username):
        userToken = db.userTokens.find_one({ 
            "email": email, 
            "token": token
        })
        if not userToken or ("verified" in userToken and userToken["verified"]):
            return False
        db.userTokens.update_one({ "_id": userToken["_id"] }, { "$set": { "verified": True } })
        return True

    def send_token(user):
        data = {
            "to": user["email"],
            "from": f"noreply@{Config.MAILGUN_DOMAIN}",
            "subject": "Verify your email!",
            "text": f"Use the token {user['token']} to verify your email.",
            "html": f"Use the token <code>{user['token']}</code> to verify your email.",
        }
        send_user_confirmation.delay(data)
