from django.db import models
from django.contrib.auth.models import User

from backend.apps.people.models import People


class Car(models.Model):
    fabula = models.TextField(verbose_name="Фабула", null=True, blank=True)
    people = models.ManyToManyField(People, verbose_name="Подозреваемый", null=True, blank=True)
    brand = models.CharField(max_length=255, verbose_name='Марка машины', null=True, blank=True)
    vin_number = models.CharField(max_length=255, verbose_name='Номер', unique=True, null=True, blank=True)
    number = models.CharField(max_length=255, verbose_name='ГОС номер', unique=True, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'добавить'
        verbose_name_plural = 'Авто транспорт'

    def __str__(self):
        return str(self.brand)


class CarImage(models.Model):
    product = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Фото",)
    image_car = models.ImageField(upload_to="src/images/car", verbose_name="Путь к фотографиям")

    class Meta:
        verbose_name = "Добавить дополнительные фотографии"
