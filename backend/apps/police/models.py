from django.db import models


class Initiator(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Ф.И.О')
    job_title = models.CharField(max_length=255, verbose_name='Должность')
    organ = models.CharField(max_length=255, verbose_name='Орган')

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'добавить'
        verbose_name_plural = 'АИС Инициатор'

    def __str__(self):
        return str(self.fullname)
