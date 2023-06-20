from django.db import models


class View(models.Model):
    title_category = models.CharField("виды", max_length=250, unique=True)

    class Meta:
        verbose_name = "номер"
        verbose_name_plural = "Дело"

    def __str__(self):
        return self.title_category


class Case(models.Model):
    vid_title = models.ForeignKey(View, verbose_name="Вид преступления", on_delete=models.CASCADE)
    title_number = models.CharField('Номер уголовного дела', max_length=250)

    class Meta:
        verbose_name = "номер"
        verbose_name_plural = "Номер уголовного дела"

    def __str__(self):
        return self.title_number