from django.db import models


class Product(models.Model):
    title = models.CharField('Наименование ', max_length=255)
    code = models.CharField('Серийный Номер', max_length=255, unique=True)
    description = models.TextField('Примичание', null=True, blank=True)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    file = models.FileField(upload_to='file', null=True, blank=True)

    date = models.DateTimeField('Дата', auto_now_add=True)
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = "продукт"
        verbose_name_plural = "АИСПП"