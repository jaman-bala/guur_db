# Generated by Django 4.2.1 on 2023-06-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuldb', '0005_remove_category_title_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_number',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='номер УД'),
            preserve_default=False,
        ),
    ]
