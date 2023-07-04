from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class People(models.Model):
    fabula = models.TextField(verbose_name="Фабула", null=True, blank=True)
    inn = models.DecimalField(max_digits=14, decimal_places=0, verbose_name='ИНН', unique=True, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name='Дата рождения', default=timezone.now, null=True, blank=True)
    nationality = models.CharField(verbose_name='Национальность', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Примичание', null=True, blank=True)
    hobby = models.TextField(verbose_name='Хобби', null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', blank=True, null=True, upload_to='src/images/people')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        ordering = ["-created"]
        verbose_name = 'добавить'
        verbose_name_plural = 'Данные подозреваемого'

    def __str__(self):
        return f"{self.inn} - {self.last_name} {self.first_name} {self.middle_name}"
