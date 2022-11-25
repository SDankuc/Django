from rest_framework import serializers

from .models import Weather

class WeatherSerializer(serializers.Serializer):
    class Meta:
        model = Weather
        fields = [
            "weather_id",
            "date",
            "lat",
            "lon",
            "city",
            "state",
            "temperatures"
        ]