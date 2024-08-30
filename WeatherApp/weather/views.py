from django.shortcuts import render
import requests


weather_translations = {
    'Clear': 'Ясно',
    'Clouds': 'Облачно',
    'Rain': 'Дождь',
    'Drizzle': 'Морось',
    'Thunderstorm': 'Гроза',
    'Snow': 'Снег',
    'Mist': 'Туман',
}

def index(request):
    city_info = None

    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET['city']
        appid = '19bb6890c698acd3f2cacc7d9c26f7cb'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid



        res = requests.get(url.format(city)).json()
        precipitation_en = res['weather'][0]['main']
        precipitation_ru = weather_translations.get(precipitation_en, precipitation_en)

        if 'main' in res and 'weather' in res:
            icon_code = res['weather'][0]['icon']
            icon_url = f'https://openweathermap.org/img/wn/{icon_code}.png'

            city_info = {
                'city': city,
                'temp': res['main']['temp'],
                'humidity': res['main']['humidity'],
                'icon': icon_url,
                'precipitation': precipitation_ru,
            }
    return render(request, 'weather/index.html', {'info': city_info})

import requests

def get_weekly_forecast(city):
    appid = 'YOUR_API_KEY'  
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={appid}'

    response = requests.get(url)
    if response.status_code == 200:
        forecast_data = response.json()
        return forecast_data
    else:
        return None


city = 'Almaty'  
weekly_forecast = get_weekly_forecast(city)

if weekly_forecast:
    for forecast in weekly_forecast['list']:
        date_time = forecast['dt_txt']
        temperature = forecast['main']['temp']
        print(f'Date: {date_time}, Temperature: {temperature}°C')
else:
    print('Failed to retrieve the forecast data.')

