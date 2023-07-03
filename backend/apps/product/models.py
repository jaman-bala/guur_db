from django.db import models


from backend.apps.people.models import People


class Product(models.Model):
    fabula = models.TextField(verbose_name="Фабула", null=True, blank=True)
    people = models.ManyToManyField(People, verbose_name="Персон", null=True, blank=True)
    code = models.CharField(verbose_name='Серийный номер', max_length=255, unique=True)
    title = models.CharField(verbose_name='Марка', max_length=255, null=True, blank=True)
    erp = models.CharField(verbose_name='Ноомер ЕРП', max_length=255)
    description = models.TextField(verbose_name='Примичание', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'добавить'
        verbose_name_plural = 'Данные украденных вещей'

    def __str__(self):
        return str(self.code)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="src/images/product")

