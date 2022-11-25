from rest_framework import generics


from .models import Weather
from .serializers import WeatherSerializer


class WeatherListView(generics.ListAPIView):
    queryset = Weather.objects.all().order_by('weather_id')
    serializer_class = WeatherSerializer
