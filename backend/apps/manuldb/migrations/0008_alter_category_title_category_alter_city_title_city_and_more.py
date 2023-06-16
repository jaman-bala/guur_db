# Generated by Django 4.2.1 on 2023-06-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuldb', '0007_remove_category_title_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title_category',
            field=models.CharField(max_length=250, unique=True, verbose_name='виды'),
        ),
        migrations.AlterField(
            model_name='city',
            name='title_city',
            field=models.CharField(max_length=250, unique=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='state',
            name='title_state',
            field=models.CharField(max_length=250, verbose_name='Город, район'),
        ),
    ]