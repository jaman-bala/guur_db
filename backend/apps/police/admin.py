from django.contrib import admin
from backend.apps.police.models import Initiator


@admin.register(Initiator)
class InitiatorAdmin(admin.ModelAdmin):
    list_display = [
        'fullname',
        'job_title',
        'organ',
    ]