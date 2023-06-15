# Generated by Django 4.2.1 on 2023-06-15 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_alter_people_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='car',
        ),
        migrations.RemoveField(
            model_name='people',
            name='products',
        ),
        migrations.RemoveField(
            model_name='people',
            name='weapon',
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кто')),
                ('relatives', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.people', verbose_name='Родственник')),
            ],
        ),
    ]
