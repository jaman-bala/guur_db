from django.contrib import admin
from .product import Product
from .weapons import Weapons


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
    ]


@admin.register(Weapons)
class WeaponAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
        'last_name',
        'first_name',
    ]
