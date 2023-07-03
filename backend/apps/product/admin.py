from django.contrib import admin
from django.contrib.auth import get_user

from backend.apps.product.models import Product, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2


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

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    def current_user(self, obj):
        user = get_user(self.request)
        return user.username if user.is_authenticated else 'Anonymous'
    current_user.short_description = 'Добавлено пользователем'

# {% for p in products %}
#     {% for i in p.images.all %}
#     {% endfor %}
#
# {%endfor%}