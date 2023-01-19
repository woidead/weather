import requests
# city = input('city: ')

key = '6440b74da23867d7cabf14b30f57a6bd'
Api = f'https://api.openweathermap.org/data/2.5/weather?q=osh&units=metric&appid={key}&lang=ru'
res = requests.get(Api)
data=res.json()
mm = data['weather'][0]['description']

print(mm)