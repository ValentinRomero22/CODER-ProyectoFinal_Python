# Generated by Django 4.0.4 on 2022-06-30 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_categoria_imagen_local_imagen_imagenproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
    ]