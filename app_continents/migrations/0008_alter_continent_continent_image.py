# Generated by Django 5.0.3 on 2024-03-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_continents', '0007_alter_continent_continent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='continent_image',
            field=models.ImageField(upload_to='images/', verbose_name='Continent Image'),
        ),
    ]
