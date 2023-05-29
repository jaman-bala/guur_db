from django.contrib import admin
from backend.apps.car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'vin_number',
        'number',
    ]