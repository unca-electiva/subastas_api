# Generated by Django 5.1.6 on 2025-02-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0003_alter_anuncio_categorias_alter_anuncio_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activa',
            field=models.BooleanField(default=True),
        ),
    ]
