# -*- coding: utf-8 -*-
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv

sys.path.append(dirname(__file__))
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def get_env(name):
    return os.environ[name]

class Config:

    API_VERSION = get_env("API_VERSION")

    MODE = get_env("MODE")

    DEBUG = get_env("DEBUG")

    # Mailgun config
    MAILGUN_DOMAIN = get_env("MAILGUN_DOMAIN")
    MAILGUN_DEFAULT_USER = get_env("MAILGUN_DEFAULT_USER")
    MAILGUN_KEY = get_env("MAILGUN_KEY")


class CeleryConf:

    BROKER_URL = get_env("CELERY_BROKER_URL")

    CELERY_IGNORE_RESULT = False

    CELERY_EVENT_QUEUE_EXPIRE = 60

    CELERYD_POOL_RESTARTS = True

    BROKER_HEARTBEAT = 0

    CELERY_ACCEPT_CONTENT = ["json"]

    CELERY_RESULT_BACKEND = get_env("CELERY_RESULT_BACKEND")


def get_client_config():
    return {
        'mode': Config.MODE,
        'api_version': Config.API_VERSION,
        'hash': ''
    }
