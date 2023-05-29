from django.contrib import admin
from backend.apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
        'erp',
    ]
