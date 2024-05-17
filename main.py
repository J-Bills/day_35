import requests

with open('./openweather_acc.txt') as info_file:
    contents = info_file.readlines()
    contents = [line.strip() for line in contents]


q: str
appid: str

q = input("input city name").lower()
appid = contents[2]



paramemters = {
    'q' : q,
    'appid' : appid
}


LAT = 37.739651
LONG = 121.425224

lat_parameters = {
    'lat': LAT,
    "lon":LONG,
    'appid' : appid
}



# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=paramemters)
# response.raise_for_status()

response = requests.get(f"https://api.openweathermap.org/data/2.5/forcast", params=lat_paramemters)
print(response.status_code)
data = response.json()

print(data)