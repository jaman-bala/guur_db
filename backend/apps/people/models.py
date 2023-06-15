from django.db import models
from django.utils import timezone

from backend.apps.police.models import Initiator


class People(models.Model):
    STATUS_CHOICES = (
        ('Ещё не установлено', 'Ещё не установлено'),
        ('Возбуждено', 'Возбуждено'),
        ('Остановлено', 'Остановлено'),
        ('Передано в суд', 'Передано в суд')
    )
    image = models.ImageField(verbose_name='Фото', blank=True, null=True, upload_to='src/images/people')
    inn = models.DecimalField(max_digits=14, decimal_places=0, verbose_name='ИНН', unique=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name='Дата рождения', default=timezone.now, null=True, blank=True)
    nationality = models.CharField(verbose_name='Национальность', max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус дела', choices=STATUS_CHOICES, default='Ещё не установлено')

    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(Initiator, verbose_name='Инициатор', blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        ordering = ["-created"]
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС Персоны'

    def __str__(self):
        return str(self.inn)



