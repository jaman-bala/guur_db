from django.apps import AppConfig


class PeopleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.people'
    verbose_name = 'Данные человека'
