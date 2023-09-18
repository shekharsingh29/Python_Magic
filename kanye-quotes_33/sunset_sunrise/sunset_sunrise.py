import requests
import datetime

parameters = {
    "lat":12.971599,
    "lng":77.594566,
    "formatted":0
}
response = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()

data = response.json()

print(data)
sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]
current_hour = datetime.datetime.now().hour

print(f"Sunrise Time: {sunrise} \nSunset Time: {sunset} \nCurrent Time: {current_hour}")