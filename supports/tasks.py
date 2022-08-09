from supports import models, service_celery
from suppDjango.celery import app


@app.task
def send_mailing(stats, users_id):
    service_celery.send_message_by_mail(stats, users_id)
