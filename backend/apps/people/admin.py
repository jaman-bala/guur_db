from django.contrib import admin
from backend.apps.people.models import People, PeopleImage


class PeopleImageInline(admin.StackedInline):
    model = PeopleImage
    extra = 3


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    inlines = [PeopleImageInline]
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