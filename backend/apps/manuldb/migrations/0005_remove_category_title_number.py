# Generated by Django 4.2.1 on 2023-06-14 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manuldb', '0004_category_title_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title_number',
        ),
    ]
