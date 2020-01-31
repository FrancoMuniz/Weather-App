from django.shortcuts import render
from django.urls import path
import urllib.request
import json


# Create your views here.
def weather_info_view(request):
    if request.method == 'POST':

        apiKey = 'e56375bc09a816ccaea1aa160377ba38'
        requested_city = request.POST['requestedCity']

        try:
            cityWeatherSource = json.loads(urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format("+".join(requested_city.split()), apiKey)).read())

        except urllib.error.HTTPError as err:
            print('City not found')
            cityWeatherData = {}

        else:
            cityWeatherData = {
                'city': requested_city,
                'temp': str(cityWeatherSource['main']['temp']) + "ºC",
                'status': str(cityWeatherSource['weather'][0]['main']),
                # 'icon': cityWeatherSource['weather']['icon'], #Implement get icon image
                'humidity': str(cityWeatherSource['main']['humidity']) + "%",
                'pressure': str(cityWeatherSource['main']['pressure']),

            }

    else:
        cityWeatherData = {}
    return render(request, 'weatherView.html', cityWeatherData)
