import requests
from django.shortcuts import render
from .forms import CityForm
from .models import City


def index(request):
    appid = 'c7fad4e8a0a6d9a2d009db75d289d97e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)

# lat=57&lon=-2.15
# {"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
# "base":"stations","main":{"temp":290.55,"feels_like":289.42,"temp_min":289.1,"temp_max":292.03,"pressure":1032,
# "humidity":41},"visibility":10000,"wind":{"speed":6.69,"deg":80},"clouds":{"all":0},"dt":1648304883,
# "sys":{"type":2,"id":268730,"country":"GB","sunrise":1648273787,"sunset":1648318949},"timezone":0,"id":2643743,"name":"London","cod":200}
