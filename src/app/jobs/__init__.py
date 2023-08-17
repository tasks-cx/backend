from celery import Celery
celery = Celery(__name__, autofinalize=False)


def create_celery(app):
    celery.config_from_object('config.CeleryConf')
    TaskBase = celery.Task

    class AppContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = AppContextTask

    # run finalize to process decorated tasks
    celery.finalize()
