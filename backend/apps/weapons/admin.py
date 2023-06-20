from django.contrib import admin
from backend.apps.weapons.models import Weapons


@admin.register(Weapons)
class WeaponAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
        'erp',
        'created',
    ]
    search_fields = [
        'code',
        'title',
        'erp',
        'created'
    ]