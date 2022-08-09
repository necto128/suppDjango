from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from supports import models

admin.site.register(models.Request)
admin.site.register(models.Ticket)
