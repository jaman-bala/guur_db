# Generated by Django 4.2.1 on 2023-06-14 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manuldb', '0008_alter_category_title_category_alter_city_title_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_number', models.CharField(max_length=250, verbose_name='Номер уголовного дела')),
                ('vid_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuldb.category')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'Город',
            },
        ),
    ]