from django.shortcuts import render
import requests
# Create your views here.


def main(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        key = '6440b74da23867d7cabf14b30f57a6bd'
        Api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}&lang=ru'
        res = requests.get(Api)
        data = res.json()
        temperature = (data['main']['temp'])
        tempmax = (data['main']['temp_max'])
        tempmin = (data['main']['temp_min'])
        humidity = (data['main']['humidity'])
        pressure = (data['main']['pressure'])
        feels_like = (data['main']['feels_like'])
        description = (data['weather'][0]['description'])
        speed = data['wind']['speed']
        deg = data['wind']['deg']
        name = data['name']

        return render(request, 'index.html', {'temperature': temperature, 'city': city, 'temp_max': tempmax, 'temp_min': tempmin, 'humidity': humidity, 
        'pressure': pressure, 'feels_like': feels_like, 'description':description, 'speed':speed, 'deg':deg, 'name':name })
    return render(request, 'index.html')
