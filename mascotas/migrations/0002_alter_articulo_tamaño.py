# Generated by Django 4.2.1 on 2023-06-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='tamaño',
            field=models.CharField(blank=True, max_length=8, verbose_name='Tamaño'),
        ),
    ]
