from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Supports import models

admin.site.register(models.Requests)
admin.site.register(models.Tikets)
