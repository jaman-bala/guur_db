from django.db import models


class Category(models.Model):
    title_category = models.CharField("виды", max_length=250, unique=True)

    class Meta:
        verbose_name = "деятельность"
        verbose_name_plural = "Вид преступления"

    def __str__(self):
        return self.title_category


class City(models.Model):
    title_city = models.CharField("Область", max_length=250, unique=True)

    class Meta:
        verbose_name = "область"
        verbose_name_plural = "Область"

    def __str__(self):
        return self.title_city


class State(models.Model):
    city_title = models.ForeignKey(City, on_delete=models.CASCADE)
    title_state = models.CharField('Город, район', max_length=250)

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "Город"

    def __str__(self):
        return self.title_state


class Vid(models.Model):
    vid_title = models.ForeignKey(Category, verbose_name="Вид преступления", on_delete=models.CASCADE)
    title_number = models.CharField('Номер уголовного дела', max_length=250)

    class Meta:
        verbose_name = "номер"
        verbose_name_plural = "Номер уголовного дела"

    def __str__(self):
        return self.title_number










