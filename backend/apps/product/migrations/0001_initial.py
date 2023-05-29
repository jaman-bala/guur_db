# Generated by Django 4.2.1 on 2023-05-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('police', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Серийный номер')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Марка')),
                ('erp', models.CharField(max_length=255, verbose_name='Ноомер ЕРП')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примичание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='src/images/things', verbose_name='Фото')),
                ('file', models.FileField(blank=True, null=True, upload_to='src/file/things', verbose_name='Файл')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('initiator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='police.initiator', verbose_name='Инициатор')),
                ('people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.people')),
            ],
            options={
                'verbose_name': 'добавить',
                'verbose_name_plural': 'АИС Вещи',
                'ordering': ['-created'],
            },
        ),
    ]