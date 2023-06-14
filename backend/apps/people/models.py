from django.db import models
from django.utils import timezone


from backend.apps.police.models import Initiator
from backend.apps.product.models import Product
from backend.apps.car.models import Car
from backend.apps.weapons.models import Weapons
from backend.apps.manuldb.models import Category, State, Vid


class People(models.Model):
    STATUS_CHOICES = (
        ('Ещё не установлено', 'Ещё не установлено'),
        ('Возбуждено', 'Возбуждено'),
        ('Остановлено', 'Остановлено'),
        ('Переданно в суд', 'Переданно в суд')
    )
    vidy = models.ForeignKey(Vid, verbose_name="Виды", on_delete=models.PROTECT)
    inn = models.DecimalField(max_digits=14, decimal_places=0, verbose_name='ИНН', unique=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчества', max_length=255, null=True, blank=True)
    city = models.ForeignKey(State, verbose_name='Область, город, район', null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес', max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name='Дата рождения', default=timezone.now, null=True, blank=True)
    nationality = models.CharField(verbose_name='Национальность', max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус дела', choices=STATUS_CHOICES, default='Ещё не установлено')
    products = models.ForeignKey(Product, verbose_name='Наличии предметов', null=True, blank=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='Налличии машины', null=True, blank=True, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapons, verbose_name='Наличии оружия', null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField(verbose_name='Фото', blank=True, null=True, upload_to='src/images/people')
    file = models.FileField(verbose_name='Файл', blank=True, null=True, upload_to='src/file/people')

    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(Initiator, verbose_name='Инициатор', blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        ordering = ["-created"]
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС Персоны'

    def __str__(self):
        return str(self.inn)


class PeopleImage(models.Model):
    people = models.ForeignKey(People, verbose_name="Фото", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='src/images/people')