import requests
from django.shortcuts import render
from geopy.geocoders import Nominatim


def get_weather(request):
    if request.method == "POST":
        city = request.POST.get('city')
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(city)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            api_key = 'your_api_key'

            url = f'https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={api_key}'

            try:
                response = requests.get(url)
                data = response.json()
                weather_description = data['data'][0]['weather']['description']
                context = {"weath": weather_description}
            except:
                pass
        else:
            context = {"weath": 'Location not found'}
    else:
        context = {}

    return render(request, 'index.html', context)
