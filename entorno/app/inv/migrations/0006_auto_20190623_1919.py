# Generated by Django 2.2.2 on 2019-06-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Categoría', max_length=100),
        ),
    ]
