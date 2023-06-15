from django.contrib import admin


from backend.apps.manuldb.models import Category, Vid


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title_category',
    ]


@admin.register(Vid)
class VidAdmin(admin.ModelAdmin):
    list_display = [
        'title_number',
    ]