from django.contrib import admin

from backend.apps.manuldb.case import Case, View


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = [
        'title_category',
    ]


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = [
        'title_number',
    ]




