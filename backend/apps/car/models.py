from django.db import models


# from backend.apps.people.models import People
from backend.apps.police.models import Initiator


class Car(models.Model):
    # people = models.ForeignKey(People, verbose_name="Персон", on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=255, verbose_name='Марка машины')
    vin_number = models.CharField(max_length=255, verbose_name='ВИН номер', unique=True, null=True, blank=True)
    number = models.CharField(max_length=255, verbose_name='ГОС номер', unique=True, null=True, blank=True)
    image = models.ImageField(max_length=255, upload_to='src/images/ima_car', null=True, blank=True)
    file = models.FileField(max_length=255, upload_to='src/file/file_car', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    initiator = models.ForeignKey(Initiator, verbose_name='Инициатор', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС РУАТ'

    def __str__(self):
        return str(self.brand)
