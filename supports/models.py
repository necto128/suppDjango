from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    creator = models.ForeignKey(User, name="creator", on_delete=models.CASCADE, default="0")
    topic = models.TextField(max_length=100)
    status_list = [
        ('Active', 'Active'),
        ('Disabled', 'Disabled')
    ]
    status = models.CharField(
        max_length=8,
        choices=status_list,
        default='Active',
    )


class Ticket(models.Model):
    request_id = models.ForeignKey(Request, name="request", on_delete=models.CASCADE, default="0")
    user_id = models.ForeignKey(User, name="user", on_delete=models.CASCADE, default="0")
    message = models.TextField(max_length=1000, name="message")
