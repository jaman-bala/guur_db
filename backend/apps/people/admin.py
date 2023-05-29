from django.contrib import admin
from backend.apps.people.models import People
# Register your models here.


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = [
        'inn',
        'last_name',
        'first_name',
        'middle_name',
        'created'
    ]

    search_fields = [
        'inn',
    ]