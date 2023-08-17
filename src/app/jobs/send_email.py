from config import *
from lib import decode_id
from app.jobs import celery
import requests

@celery.task
def send_user_confirmation(data):
    response = requests.post("https://api.mailgun.net/v2/%s/messages" % Config.MAILGUN_DOMAIN,
        auth=("api", Config.MAILGUN_KEY),
        data={
            "from": "%s@%s" % (Config.MAILGUN_DEFAULT_USER, Config.MAILGUN_DOMAIN),
            "to": data["email"],
            "subject": data["subject"],
            "text": data["text"],
            "html": data["html"]
        })
    if response.status_code != 200:
        return False
    return True
