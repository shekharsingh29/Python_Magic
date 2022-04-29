# reading csv data as whole

with open("weather_data.csv") as data_files:
    print('''
        File operation method
    ''')
    print(data_files.readlines())

# reading csv from csv library

import csv
with open("weather_data.csv") as data_files:
    data = csv.reader(data_files)
    print('''
        CSV Library
    ''')
    for row in data:
        print(row)

# reading from pandas

import pandas

data = pandas.read_csv("weather_data.csv")
print('''
    PANDAS Library
''')
print(data)

# printing DataFrame type
print(type(data))

# print Series type
print(type(data["temp"]))

# converting Series to list
print(data["temp"].to_list())

# Converting DataFrame to dictionary
print(data.to_dict())

# applying condition

print(data[data["temp"] == data["temp"].max()])

# applying condition and changing it to CSV

data[data['temp'] == data["temp"].min()].to_csv("cold_weather_day.csv")