from django.db import models

from backend.apps.manuldb.case import Case
from backend.apps.people.models import People


class Weapons(models.Model):
    status_number = models.ForeignKey(Case, verbose_name='Номер уголовного дело', on_delete=models.CASCADE)
    people = models.ManyToManyField(People, verbose_name="Персон", null=True, blank=True)
    code = models.CharField(verbose_name='Серийный номер', max_length=255, unique=True)
    title = models.CharField(verbose_name='Марка', max_length=255, null=True, blank=True)
    erp = models.CharField(verbose_name='Номер ЕРП', max_length=255)
    description = models.TextField(verbose_name='Примичание', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        ordering = ['-created']
        verbose_name = 'добавить'
        verbose_name_plural = 'Данные оружия'

    def __str__(self):
        return str(self.code)
