from django.db import models

from backend.apps.people.models import People


class Relatives(models.Model):
    who = models.CharField(verbose_name='Кто', max_length=255, null=True, blank=True)
    relatives = models.ManyToManyField(People, verbose_name="Родственник", related_name="related_people")
    person = models.ForeignKey(People, verbose_name="Человек", related_name="relatives", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Добавить данные"


class PeopleImage(models.Model):
    people = models.ForeignKey(People, verbose_name="Фото", on_delete=models.CASCADE)
    image_college = models.ImageField(verbose_name="Путь к фотографиям")

    class Meta:
        verbose_name = "Добавить дополнительные фотографии"


