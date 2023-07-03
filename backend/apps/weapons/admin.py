from django.contrib import admin
from django.contrib.auth import get_user

from backend.apps.weapons.models import Weapons, WeaponsImage


class WeaponsImageInline(admin.StackedInline):
    model = WeaponsImage
    extra = 2


@admin.register(Weapons)
class WeaponAdmin(admin.ModelAdmin):
    inlines = [WeaponsImageInline]
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

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    def current_user(self, obj):
        user = get_user(self.request)
        return user.username if user.is_authenticated else 'Anonymous'
    current_user.short_description = 'Добавлено пользователем'