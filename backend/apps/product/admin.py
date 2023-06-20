from django.contrib import admin
from backend.apps.product.models import Product, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = [
        'code',
        'title',
        'erp',
    ]
    search_fields = [
        'code',
        'title',
        'created'
    ]

# {% for p in products %}
#     {% for i in p.images.all %}
#     {% endfor %}
#
# {%endfor%}