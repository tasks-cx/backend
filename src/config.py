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
    HOST = get_env("HOST")
    MODE = get_env("MODE")
    DEBUG = get_env("DEBUG")

    # Mailgun config
    MAILGUN_DOMAIN = get_env("MAILGUN_DOMAIN")
    MAILGUN_DEFAULT_USER = get_env("MAILGUN_DEFAULT_USER")
    MAILGUN_KEY = get_env("MAILGUN_KEY")

    MONGO_DATABASE = get_env("MONGO_INITDB_ROOT_DATABASE")
    MONGO_HOST = get_env("MONGO_INITDB_ROOT_HOST")
    MONGO_PORT = get_env("MONGO_INITDB_ROOT_PORT")
    MONGO_USERNAME = get_env("MONGO_INITDB_ROOT_USERNAME")
    MONGO_PASSWORD = get_env("MONGO_INITDB_ROOT_PASSWORD")

    CONNECTION_STR = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
    CELERY_BROKER_URL = CONNECTION_STR
    CELERY_RESULT_BACKEND = CONNECTION_STR
    CELERY_CONFIG = dict(
        broker_url=CONNECTION_STR,
        result_backend=CONNECTION_STR,
        task_ignore_result=True,
    )

def get_client_config():
    return {
        'mode': Config.MODE,
        'api_version': Config.API_VERSION,
        'hash': ''
    }
