from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user

from backend.apps.manuldb.models import PeopleImage, Relatives
from backend.apps.people.models import People


class RelativesInline(admin.StackedInline):
    model = Relatives
    extra = 2


class PeopleImageInline(admin.StackedInline):
    readonly_fields = ["Фотографии"]
    model = PeopleImage
    extra = 3

    def Фотографии(self, obj):
        return mark_safe(f'<img src="{obj.image_college.url}" style="max-height: 330px;">')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    inlines = [PeopleImageInline, RelativesInline]
    readonly_fields = ["Аватар"]

    def Аватар(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 330px;">')



    list_display = [
        'inn',
        'last_name',
        'first_name',
        'middle_name',
        'created',
        'current_user',
    ]

    search_fields = [
        'inn',
        'last_name',
        'first_name',
        'middle_name',
        'created'
    ]

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    def current_user(self, obj):
        user = get_user(self.request)
        return user.username if user.is_authenticated else 'Anonymous'
    current_user.short_description = 'Добавлено пользователем'


admin.site.site_header = 'БИРДИКТУУ БАЗА'
admin.site.index_title = 'СПИСОК БАЗЫ'