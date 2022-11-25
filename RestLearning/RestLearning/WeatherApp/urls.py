from django.urls import path

from . import views

urlpatterns = [
    path("", views.WeatherListView.as_view())
]
