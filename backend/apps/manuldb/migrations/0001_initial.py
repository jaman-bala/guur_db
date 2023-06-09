# Generated by Django 4.2.1 on 2023-07-04 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кто')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatives', to='people.people', verbose_name='Человек')),
                ('relatives', models.ManyToManyField(related_name='related_people', to='people.people', verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Добавить данные',
            },
        ),
        migrations.CreateModel(
            name='PeopleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_college', models.ImageField(upload_to='', verbose_name='Путь к фотографиям')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.people', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Добавить дополнительные фотографии',
            },
        ),
    ]
