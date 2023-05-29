from django.db import models
from dal import autocomplete


from backend.apps.people.models import People
from backend.apps.police.models import Initiator


class Product(models.Model):
    people = models.ForeignKey(
        People,
        verbose_name="Персон",
        on_delete=models.SET_NULL,
        null=True,
    )
    code = models.CharField(verbose_name='Серийный номер', max_length=255, unique=True)
    title = models.CharField(verbose_name='Марка', max_length=255, null=True, blank=True)
    erp = models.CharField(verbose_name='Ноомер ЕРП', max_length=255)
    description = models.TextField(verbose_name='Примичание', null=True, blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='src/images/things', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='src/file/things', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    initiator = models.ForeignKey(
        Initiator,
        verbose_name='Инициатор',
        blank=True, null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС Вещи'

    def __str__(self):
        return str(self.code)



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="products/images")

