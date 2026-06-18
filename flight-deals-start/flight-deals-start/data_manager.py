import requests
import json
import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        pass

    def get_flight_data(self):
        response = requests.get("https://api.sheety.co/e2e34e2664b6d873eb7e7d4fb4480c03/flightDeals/prices")
        response.raise_for_status()
        flight_data = response.json()
        pp =  pprint.PrettyPrinter(indent=4)
        pp.pprint(flight_data)
        return flight_data['prices']
    
    def update_flight_data(self,city):
        new_data = {
                "price": {
                    "iataCode": city["iataCode"]
            }
        }
        update_url = f"https://api.sheety.co/e2e34e2664b6d873eb7e7d4fb4480c03/flightDeals/prices/{city['id']}"
        response = requests.put(update_url,json=new_data)
        response.raise_for_status()
        return response