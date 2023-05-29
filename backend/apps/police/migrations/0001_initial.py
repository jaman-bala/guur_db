# Generated by Django 4.2.1 on 2023-05-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Initiator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Ф.И.О')),
                ('job_title', models.CharField(max_length=255, verbose_name='Должность')),
                ('organ', models.CharField(max_length=255, verbose_name='Орган')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'добавить',
                'verbose_name_plural': 'АИС Инициатор',
            },
        ),
    ]
