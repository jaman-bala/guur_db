from django.contrib import admin
from django.contrib.auth import get_user
from django.utils.safestring import mark_safe


from backend.apps.car.models import Car, CarImage


class CarImageInline(admin.StackedInline):
    readonly_fields = ["Фотографии"]
    model = CarImage
    extra = 2

    def Фотографии(self, obj):
        return mark_safe(f'<img src="{obj.image_car.url}" style="max-height: 330px;">')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = [
        'brand',
        'vin_number',
        'number',
        'current_user',
    ]

    search_fields = [
        'brand',
        'vin_number',
        'number',
        'created'
        'current_user__username',
    ]

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    def current_user(self, obj):
        user = get_user(self.request)
        return user.username if user.is_authenticated else 'Anonymous'
    current_user.short_description = 'Добавлено пользователем'