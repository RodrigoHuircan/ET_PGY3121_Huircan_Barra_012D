# Generated by Django 4.2.1 on 2023-07-13 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_alter_articulo_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stock'),
        ),
    ]
