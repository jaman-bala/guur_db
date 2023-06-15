from django.contrib import admin
from django.utils.safestring import mark_safe

from backend.apps.manuldb.models import PeopleImage, Relatives
from backend.apps.people.models import People


class RelativesInline(admin.StackedInline):
    model = Relatives
    extra = 2


class PeopleImageInline(admin.StackedInline):
    model = PeopleImage
    extra = 3


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    inlines = [PeopleImageInline, RelativesInline]
    readonly_fields = ["avatar"]

    def avatar(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 330px;">')

    list_display = [
        'inn',
        'last_name',
        'first_name',
        'middle_name',
        'created',
        'image',
    ]

    search_fields = [
        'inn',
        'last_name',
        'first_name',
        'middle_name',
        'created'
    ]

