import requests
from datetime import datetime

MY_LAT = 12.971599 # Your latitude
MY_LONG = 77.594566 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
current_hour = int(datetime.now().hour)

time_now = datetime.now()

def distance_from_me():
    if (MY_LAT >= iss_latitude-5 and MY_LAT <= iss_latitude+5) and (MY_LONG >= iss_longitude-5 and MY_LONG <= iss_longitude+5):
        return True 
    else:
        return False

def is_dark():
    if current_hour>sunset and current_hour<sunrise:
        return True
    else:
        return False

#If the ISS is close to my current position
close_status = distance_from_me()
# and it is currently dark
dark_status = is_dark()
# Then send me an email to tell me to look up.
if dark_status and close_status:
    print("Go out and watch the show")
else:
    print("Sit back and study")
# BONUS: run the code every 60 seconds.



