# Generated by Django 4.1.3 on 2022-11-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='weather_id',
            field=models.IntegerField(editable=False, unique=True),
        ),
    ]
