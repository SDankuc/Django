from django.db import models

# Create your models here.

class Weather(models.Model):
    weather_id = models.IntegerField(unique=True, editable=False)
    date = models.DateField(default= None)
    lat = models.DecimalField(max_digits=6,decimal_places=4)
    lon = models.DecimalField(max_digits=6,decimal_places=4)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    temperatures = models.JSONField()
