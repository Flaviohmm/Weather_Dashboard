from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

def index(request):
    api_key = '1e2131138735d9551c37916c241825a8'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form
    }

    return render(request, 'weather/index.html', context)

