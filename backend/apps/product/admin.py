from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user

from backend.apps.product.models import Product, ProductImage


class ProductImageInline(admin.StackedInline):
    readonly_fields = ["Изображения"]
    model = ProductImage
    extra = 2

    def Изображения(self, obj):
        return mark_safe(f'<img src="{obj.image_product.url}" style="max-height: 330px;">')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = [
        'code',
        'title',
        'erp',
        'created'
    ]
    search_fields = [
        'code',
        'title',
        'fabula',
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

# {% for p in products %}
#     {% for i in p.images.all %}
#     {% endfor %}
#
# {%endfor%}