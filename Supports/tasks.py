from Supports import models, service
from suppDjango.celery import app


@app.task
def send_mailing(stats, users_id):
    service.send(stats, users_id)
