# Gets you the international space station position

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

position=(longitude,latitude)

print(f"The current position of international space station {position}")

