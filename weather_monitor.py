import requests
from datetime import datetime

API_KEY = '6ac56b1b68a4f78da1ec97c8725b075a'
city = 'Delhi'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response = requests.get(url)
data = response.json()
temp = data['main']['temp']

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if temp > 35:
    message = f'[{now}] ALERT: {city} temp is {temp}C - Too hot!'
elif temp > 25:
    message = f'[{now}] WARNING: {city} temp is {temp}C - Getting warm'
else:
    message = f'[{now}] OK: {city} temp is {temp}C - Normal'

print(message)

with open('weather_log.txt', 'a') as log:
    log.write(message + '\n')
