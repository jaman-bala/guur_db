from django.db import models

from backend.apps.people.models import People


class Category(models.Model):
    title_category = models.CharField("виды", max_length=250, unique=True)

    class Meta:
        verbose_name = "деятельность"
        verbose_name_plural = "Вид преступления"

    def __str__(self):
        return self.title_category


class Vid(models.Model):
    vid_title = models.ForeignKey(Category, verbose_name="Вид преступления", on_delete=models.CASCADE)
    title_number = models.CharField('Номер уголовного дела', max_length=250)

    class Meta:
        verbose_name = "номер"
        verbose_name_plural = "Номер уголовного дела"

    def __str__(self):
        return self.title_number


class Relatives(models.Model):
    who = models.CharField(verbose_name='Кто', max_length=255, null=True, blank=True)
    relatives = models.ManyToManyField(People, verbose_name="Родственник", related_name="related_people")
    person = models.ForeignKey(People, verbose_name="Человек", related_name="relatives", on_delete=models.CASCADE)


class PeopleImage(models.Model):
    people = models.ForeignKey(People, verbose_name="Фото", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='src/images/people', verbose_name="Фото")

    class Meta:
        verbose_name = "Добавить дополнительные фотографии"









