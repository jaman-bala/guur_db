# Generated by Django 4.2.1 on 2023-05-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование ')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Серийный Номер')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примичание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('file', models.FileField(blank=True, null=True, upload_to='file')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'АИСПП',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Модель оружии')),
                ('code', models.CharField(max_length=255, verbose_name='Серийный Номер')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примичание')),
                ('inn', models.DecimalField(decimal_places=0, max_digits=14, unique=True, verbose_name='ИНН')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('age', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Фото')),
                ('file', models.FileField(blank=True, null=True, upload_to='file', verbose_name='Файл')),
                ('initiator', models.CharField(max_length=255, verbose_name='ФИО Иницатора')),
                ('rank', models.CharField(max_length=255, verbose_name='Звание')),
                ('organ', models.CharField(max_length=255, verbose_name='ГОС орган')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'оружия',
                'verbose_name_plural': 'АИС Оружия',
                'ordering': ['-date'],
            },
        ),
    ]
