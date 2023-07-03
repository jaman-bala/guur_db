# Generated by Django 4.2.1 on 2023-07-03 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вид преступления')),
                ('fabula', models.CharField(blank=True, max_length=22255, null=True, verbose_name='Фабула')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Марка машины')),
                ('vin_number', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Номер')),
                ('number', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='ГОС номер')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('people', models.ManyToManyField(blank=True, null=True, to='people.people', verbose_name='Персон')),
            ],
            options={
                'verbose_name': 'добавить',
                'verbose_name_plural': 'Авто транспорт',
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_car', models.ImageField(upload_to='src/images/car', verbose_name='Путь к фотографиям')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Добавить дополнительные фотографии',
            },
        ),
    ]
