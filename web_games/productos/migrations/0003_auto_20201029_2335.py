# Generated by Django 3.1.1 on 2020-10-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20201029_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos', verbose_name='Imagen del Producto'),
        ),
    ]