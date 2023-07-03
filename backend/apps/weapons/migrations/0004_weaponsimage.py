# Generated by Django 4.2.1 on 2023-07-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0003_weapons_fabula'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeaponsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_car', models.ImageField(upload_to='src/images/цeapons', verbose_name='Путь к фотографиям')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapons', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Добавить дополнительные фотографии',
            },
        ),
    ]