from celery import shared_task
import requests
from config import *

@shared_task(ignore_result=True)
def send_user_confirmation(data):
    response = requests.post("https://api.mailgun.net/v2/%s/messages" % Config.MAILGUN_DOMAIN,
        auth=("api", Config.MAILGUN_KEY),
        data={
            "from": data["from"],
            "to": data["to"],
            "subject": data["subject"],
            "text": data["text"],
            "html": data["html"]
        })
    if response.status_code != 200:
        return False
    return True
