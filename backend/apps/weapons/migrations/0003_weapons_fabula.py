# Generated by Django 4.2.1 on 2023-07-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_remove_weapons_fabula_remove_weapons_vid'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapons',
            name='fabula',
            field=models.TextField(blank=True, null=True, verbose_name='Фабула'),
        ),
    ]