from django.db import models


class Weapons(models.Model):
    title = models.CharField('Модель оружии', max_length=255)
    code = models.CharField('Серийный Номер', max_length=255)
    description = models.TextField('Примичание', null=True, blank=True)

    inn = models.DecimalField('ИНН', max_digits=14, decimal_places=0, unique=True)
    last_name = models.CharField('Фамилия', max_length=255)
    first_name = models.CharField('Имя', max_length=255)
    middle_name = models.CharField('Отчество', max_length=255, null=True, blank=True)
    adress = models.CharField('Адрес', max_length=255, null=True, blank=True)
    city = models.CharField('Город', max_length=255, null=True, blank=True)
    age = models.DateField('Дата рождения', null=True, blank=True)
    image = models.ImageField(upload_to='img', null=True, blank=True, verbose_name='Фото')
    file = models.FileField(upload_to='file', null=True, blank=True, verbose_name='Файл')

    initiator = models.CharField(max_length=255, verbose_name='ФИО Иницатора')
    rank = models.CharField(max_length=255, verbose_name='Звание')
    organ = models.CharField(max_length=255, verbose_name='ГОС орган')

    is_active = models.BooleanField('Активный', default=True)
    date = models.DateTimeField('Дата', auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = "оружия"
        verbose_name_plural = "АИС Оружия"




