#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_flight_data()
print("Flight Details::")
pprint(sheet_data)

# Update wherever IATA is empty
# Update new IATA in google sheet

flight_search_data = FlightSearch()

for index,city in enumerate(sheet_data):
    if city['iataCode'] == '':
        city['iataCode'] = flight_search_data.getIataCode()
        data_manager.update_flight_data(city)

print("Flight Details after updating iataCode::")
pprint(sheet_data)














