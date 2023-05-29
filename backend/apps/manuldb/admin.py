from django.contrib import admin


from backend.apps.manuldb.models import Category, State, City


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title_category',
    ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'title_city',
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'title_state',
    ]