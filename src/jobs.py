from app import create_app

taskscx = create_app()
celery_app = taskscx.extensions["celery"]