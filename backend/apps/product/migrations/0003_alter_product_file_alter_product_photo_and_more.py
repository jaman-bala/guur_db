# Generated by Django 4.2.1 on 2023-06-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_people_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='src/file/product', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='src/images/product', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='src/images/product'),
        ),
    ]