from django.db import models
from django.contrib.auth.models import User

from backend.apps.people.models import People
from backend.apps.manuldb.case import Case


class Car(models.Model):
    status_number = models.ForeignKey(Case, verbose_name='Номер уголовного дело', on_delete=models.CASCADE)
    people = models.ManyToManyField(People, verbose_name="Персон", null=True, blank=True)
    brand = models.CharField(max_length=255, verbose_name='Марка машины')
    vin_number = models.CharField(max_length=255, verbose_name='ВИН номер', unique=True, null=True, blank=True)
    number = models.CharField(max_length=255, verbose_name='ГОС номер', unique=True, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

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
