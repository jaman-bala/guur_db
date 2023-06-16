# Generated by Django 4.2.1 on 2023-05-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_people_status'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.people', verbose_name='Персон'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]