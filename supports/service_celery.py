from django.core.mail import send_mail
import suppDjango.settings as siting
from supports import models


def send_message_by_mail(stats, users_id):
    recipient = models.User.objects.get(id=users_id).email
    send_mail("Support",
              f"Your request status has been changed to {stats}",
              siting.EMAIL_HOST_USER,
              [recipient],
              fail_silently=False,
              )
