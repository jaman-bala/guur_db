from django.db import models

from backend.apps.people.models import People


class Weapons(models.Model):
    fabula = models.TextField(verbose_name="Фабула", null=True, blank=True)
    people = models.ManyToManyField(People, verbose_name="Подозреваемый", null=True, blank=True)
    code = models.CharField(verbose_name='Серийный номер', max_length=255, unique=True)
    title = models.CharField(verbose_name='Марка', max_length=255, null=True, blank=True)
    erp = models.CharField(verbose_name='Номер ЕРП', max_length=255)
    description = models.TextField(verbose_name='Примичание', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        ordering = ['-created']
        verbose_name = 'добавить'
        verbose_name_plural = 'Данные оружия'

    def __str__(self):
        return str(self.code)


class WeaponsImage(models.Model):
    product = models.ForeignKey(Weapons, on_delete=models.CASCADE, verbose_name="Фото",)
    image_weapons = models.ImageField(upload_to="src/images/weapons", verbose_name="Путь к фотографиям")

    class Meta:
        verbose_name = "Добавить дополнительные фотографии"
