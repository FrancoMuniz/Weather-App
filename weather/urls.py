from django.urls import path
from .views import ( 
    weather_info_view,
)


app_name = 'weather'

urlpatterns = [
    path('',  weather_info_view, name='weather-view'),
]