# Generated by Django 4.2.1 on 2023-06-14 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0003_remove_weapons_people'),
        ('car', '0003_remove_car_people'),
        ('product', '0004_remove_product_people'),
        ('people', '0008_remove_people_car_remove_people_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car', verbose_name='Налличии машины'),
        ),
        migrations.AlterField(
            model_name='people',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Наличии предметов'),
        ),
        migrations.AlterField(
            model_name='people',
            name='weapon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weapons.weapons', verbose_name='Наличии оружия'),
        ),
    ]
