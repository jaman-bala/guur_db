from django.db import models
from django.utils import timezone


from backend.apps.police.models import Initiator
from backend.apps.manuldb.models import Category, State


class People(models.Model):
    STATUS_CHOICES = (
        ('organization', 'Организатор'),
        ('glavar', 'Главарь'),
        ('shesterka', 'Шестерка')
    )
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    inn = models.DecimalField(max_digits=14, decimal_places=0, verbose_name='ИНН', unique=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчества', max_length=255, null=True, blank=True)
    city = models.ForeignKey(State, verbose_name='Область, город, район', null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес', max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name='Дата рождения', default=timezone.now, null=True, blank=True)
    nationality = models.CharField(verbose_name='Национальность', max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICES, default='organization')

    image = models.ImageField(verbose_name='Фото', blank=True, null=True, upload_to='src/images/people')
    file = models.FileField(verbose_name='Файл', blank=True, null=True, upload_to='src/file/people')

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    initiator = models.ForeignKey(Initiator, verbose_name='Инициатор', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС Персоны'

    def __str__(self):
        return str(self.inn)


class PeopleImage(models.Model):
    people = models.ForeignKey(People, verbose_name="Фото", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='src/images/people')