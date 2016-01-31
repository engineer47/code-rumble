from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ..models import Job


class JobAdmin(ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
