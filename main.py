import requests
import os
from twilio.rest import Client


with open('./openweather_acc.txt', 'r') as info_file:
    contents = info_file.readlines()
    contents = [line.strip() for line in contents]
    
with open('./twilio_acc.txt', 'r') as twilio_info:
    secrets = twilio_info.readlines()
    secrets = [line.strip() for line in secrets]
    
twilio = {
    'account_sid': secrets[0],
    'auth_token': secrets[1],
    'num': secrets[2]
}

q: str
appid: str

# q = input("input city name").lower()
appid = contents[2]



# paramemters = {
#     'q' : q,
#     'appid' : appid
# }


LAT = 37.739651
LONG = 121.425224

lat_parameters = {
    'lat': LAT,
    "lon":LONG,
    'appid' : appid,
    'cnt': 4
}

client = Client(twilio.get('account_sid'), twilio.get('auth_token'))




# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=paramemters)
# response.raise_for_status()

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=lat_parameters)
print(response.status_code)
data = response.json()


weather_id_list = list()
for num in range(0,3):
    weather_id = data['list'][num]['weather'][0]['id']
    weather_id_list.append(weather_id)
    
print(weather_id_list)

print(twilio)
    
if any(weather_id > 700 for weather_id in weather_id_list):
    message = client.messages \
                .create(
                    body="Lovely Day Today",
                    from_=twilio.get('num'),
                    to='+11111111'
                )

print(message.sid)


