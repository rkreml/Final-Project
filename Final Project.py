#EPSY 5200 Final Project Python Script File
#Author: Robert T. Kreml

Version = "1.1.0"
Date = "December 17, 2019"

print(f"Thank you for running this script! This is in partial fulfillment of the requirements for EPSY 5200 for the Fall 2019 Semester.")
print(f"You are currently running version: {Version}, created on: {Date}.")

import urllib.request
import urllib.parse
import json
import statistics
import pandas as pd
import sys

city = input("Please type in the city you would like to get the weather for or type 'NA' to cancel: ")
if city == 'NA':
    sys.exit()

params = {"appid":"7d8615fc2e5e528e24c0a03e480f10e1", "q": city, "units": "imperial"}
arguments = urllib.parse.urlencode(params)

address = "http://api.openweathermap.org/data/2.5/forecast"
url = address + "?" + arguments

webData = urllib.request.urlopen(url)
results = webData.read().decode('UTF-8')
webData.close()

data = json.loads(results)

# print(data["list"][0]["main"]["temp_min"])

## DAY 1 DATA

# creating the first day of the forecast minimum temperatures
day_1_min = []

day_1_min.append(data["list"][0]["main"]["temp_min"])
day_1_min.append(data["list"][1]["main"]["temp_min"])
day_1_min.append(data["list"][2]["main"]["temp_min"])
day_1_min.append(data["list"][3]["main"]["temp_min"])
day_1_min.append(data["list"][4]["main"]["temp_min"])
day_1_min.append(data["list"][5]["main"]["temp_min"])
day_1_min.append(data["list"][6]["main"]["temp_min"])
day_1_min.append(data["list"][7]["main"]["temp_min"])

day_1_min_mean = statistics.mean(day_1_min)
day_1_min_mean = round(day_1_min_mean, ndigits = 2)

# creating the first day of the forecast maximum temperatures
day_1_max = []

day_1_max.append(data["list"][0]["main"]["temp_max"])
day_1_max.append(data["list"][1]["main"]["temp_max"])
day_1_max.append(data["list"][2]["main"]["temp_max"])
day_1_max.append(data["list"][3]["main"]["temp_max"])
day_1_max.append(data["list"][4]["main"]["temp_max"])
day_1_max.append(data["list"][5]["main"]["temp_max"])
day_1_max.append(data["list"][6]["main"]["temp_max"])
day_1_max.append(data["list"][7]["main"]["temp_max"])

day_1_max_mean = statistics.mean(day_1_max)
day_1_max_mean = round(day_1_max_mean, ndigits = 2)

# creating the first day of the forecast humidity
day_1_hum = []

day_1_hum.append(data["list"][0]["main"]["humidity"])
day_1_hum.append(data["list"][1]["main"]["humidity"])
day_1_hum.append(data["list"][2]["main"]["humidity"])
day_1_hum.append(data["list"][3]["main"]["humidity"])
day_1_hum.append(data["list"][4]["main"]["humidity"])
day_1_hum.append(data["list"][5]["main"]["humidity"])
day_1_hum.append(data["list"][6]["main"]["humidity"])
day_1_hum.append(data["list"][7]["main"]["humidity"])

day_1_hum_mean = statistics.mean(day_1_hum)
day_1_hum_mean = round(day_1_hum_mean, ndigits = 2)

## DAY 2 DATA

# creating the second day of the forecast minimum temperatures
day_2_min = []

day_2_min.append(data["list"][8]["main"]["temp_min"])
day_2_min.append(data["list"][9]["main"]["temp_min"])
day_2_min.append(data["list"][10]["main"]["temp_min"])
day_2_min.append(data["list"][11]["main"]["temp_min"])
day_2_min.append(data["list"][12]["main"]["temp_min"])
day_2_min.append(data["list"][13]["main"]["temp_min"])
day_2_min.append(data["list"][14]["main"]["temp_min"])
day_2_min.append(data["list"][15]["main"]["temp_min"])

day_2_min_mean = statistics.mean(day_2_min)
day_2_min_mean = round(day_2_min_mean, ndigits = 2)

# creating the second day of the forecast maximum temperatures
day_2_max = []

day_2_max.append(data["list"][8]["main"]["temp_max"])
day_2_max.append(data["list"][9]["main"]["temp_max"])
day_2_max.append(data["list"][10]["main"]["temp_max"])
day_2_max.append(data["list"][11]["main"]["temp_max"])
day_2_max.append(data["list"][12]["main"]["temp_max"])
day_2_max.append(data["list"][13]["main"]["temp_max"])
day_2_max.append(data["list"][14]["main"]["temp_max"])
day_2_max.append(data["list"][15]["main"]["temp_max"])

day_2_max_mean = statistics.mean(day_2_max)
day_2_max_mean = round(day_2_max_mean, ndigits = 2)

# creating the second day of the forecast humidity
day_2_hum = []

day_2_hum.append(data["list"][8]["main"]["humidity"])
day_2_hum.append(data["list"][9]["main"]["humidity"])
day_2_hum.append(data["list"][10]["main"]["humidity"])
day_2_hum.append(data["list"][11]["main"]["humidity"])
day_2_hum.append(data["list"][12]["main"]["humidity"])
day_2_hum.append(data["list"][13]["main"]["humidity"])
day_2_hum.append(data["list"][14]["main"]["humidity"])
day_2_hum.append(data["list"][15]["main"]["humidity"])

day_2_hum_mean = statistics.mean(day_2_hum)
day_2_hum_mean = round(day_2_hum_mean, ndigits = 2)

## DAY 3 DATA

# creating the third day of the forecast minimum temperatures
day_3_min = []

day_3_min.append(data["list"][16]["main"]["temp_min"])
day_3_min.append(data["list"][17]["main"]["temp_min"])
day_3_min.append(data["list"][18]["main"]["temp_min"])
day_3_min.append(data["list"][19]["main"]["temp_min"])
day_3_min.append(data["list"][20]["main"]["temp_min"])
day_3_min.append(data["list"][21]["main"]["temp_min"])
day_3_min.append(data["list"][22]["main"]["temp_min"])
day_3_min.append(data["list"][23]["main"]["temp_min"])

day_3_min_mean = statistics.mean(day_3_min)
day_3_min_mean = round(day_3_min_mean, ndigits = 2)

# creating the third day of the forecast maximum temperatures
day_3_max = []

day_3_max.append(data["list"][16]["main"]["temp_max"])
day_3_max.append(data["list"][17]["main"]["temp_max"])
day_3_max.append(data["list"][18]["main"]["temp_max"])
day_3_max.append(data["list"][19]["main"]["temp_max"])
day_3_max.append(data["list"][20]["main"]["temp_max"])
day_3_max.append(data["list"][21]["main"]["temp_max"])
day_3_max.append(data["list"][22]["main"]["temp_max"])
day_3_max.append(data["list"][23]["main"]["temp_max"])

day_3_max_mean = statistics.mean(day_3_max)
day_3_max_mean = round(day_3_max_mean, ndigits = 2)

# creating the third day of the forecast humidity
day_3_hum = []

day_3_hum.append(data["list"][16]["main"]["humidity"])
day_3_hum.append(data["list"][17]["main"]["humidity"])
day_3_hum.append(data["list"][18]["main"]["humidity"])
day_3_hum.append(data["list"][19]["main"]["humidity"])
day_3_hum.append(data["list"][20]["main"]["humidity"])
day_3_hum.append(data["list"][21]["main"]["humidity"])
day_3_hum.append(data["list"][22]["main"]["humidity"])
day_3_hum.append(data["list"][23]["main"]["humidity"])

day_3_hum_mean = statistics.mean(day_3_hum)
day_3_hum_mean = round(day_3_hum_mean, ndigits = 2)

## DAY 4 DATA

# creating the fourth day of the forecast minimum temperatures
day_4_min = []

day_4_min.append(data["list"][24]["main"]["temp_min"])
day_4_min.append(data["list"][25]["main"]["temp_min"])
day_4_min.append(data["list"][26]["main"]["temp_min"])
day_4_min.append(data["list"][27]["main"]["temp_min"])
day_4_min.append(data["list"][28]["main"]["temp_min"])
day_4_min.append(data["list"][29]["main"]["temp_min"])
day_4_min.append(data["list"][30]["main"]["temp_min"])
day_4_min.append(data["list"][31]["main"]["temp_min"])

day_4_min_mean = statistics.mean(day_4_min)
day_4_min_mean = round(day_4_min_mean, ndigits = 2)

# creating the fourth day of the forecast maximum temperatures
day_4_max = []

day_4_max.append(data["list"][24]["main"]["temp_max"])
day_4_max.append(data["list"][25]["main"]["temp_max"])
day_4_max.append(data["list"][26]["main"]["temp_max"])
day_4_max.append(data["list"][27]["main"]["temp_max"])
day_4_max.append(data["list"][28]["main"]["temp_max"])
day_4_max.append(data["list"][29]["main"]["temp_max"])
day_4_max.append(data["list"][30]["main"]["temp_max"])
day_4_max.append(data["list"][31]["main"]["temp_max"])

day_4_max_mean = statistics.mean(day_4_max)
day_4_max_mean = round(day_4_max_mean, ndigits = 2)

# creating the fourth day of the forecast humidity
day_4_hum = []

day_4_hum.append(data["list"][24]["main"]["humidity"])
day_4_hum.append(data["list"][25]["main"]["humidity"])
day_4_hum.append(data["list"][26]["main"]["humidity"])
day_4_hum.append(data["list"][27]["main"]["humidity"])
day_4_hum.append(data["list"][28]["main"]["humidity"])
day_4_hum.append(data["list"][29]["main"]["humidity"])
day_4_hum.append(data["list"][30]["main"]["humidity"])
day_4_hum.append(data["list"][31]["main"]["humidity"])

day_4_hum_mean = statistics.mean(day_4_hum)
day_4_hum_mean = round(day_4_hum_mean, ndigits = 2)

## DAY 5 DATA

# creating the fifth day of the forecast minimum temperatures
day_5_min = []

day_5_min.append(data["list"][32]["main"]["temp_min"])
day_5_min.append(data["list"][33]["main"]["temp_min"])
day_5_min.append(data["list"][34]["main"]["temp_min"])
day_5_min.append(data["list"][35]["main"]["temp_min"])
day_5_min.append(data["list"][36]["main"]["temp_min"])
day_5_min.append(data["list"][37]["main"]["temp_min"])
day_5_min.append(data["list"][38]["main"]["temp_min"])
day_5_min.append(data["list"][39]["main"]["temp_min"])

day_5_min_mean = statistics.mean(day_5_min)
day_5_min_mean = round(day_5_min_mean, ndigits = 2)

# creating the fifth day of the forecast maximum temperatures
day_5_max = []

day_5_max.append(data["list"][32]["main"]["temp_max"])
day_5_max.append(data["list"][33]["main"]["temp_max"])
day_5_max.append(data["list"][34]["main"]["temp_max"])
day_5_max.append(data["list"][35]["main"]["temp_max"])
day_5_max.append(data["list"][36]["main"]["temp_max"])
day_5_max.append(data["list"][37]["main"]["temp_max"])
day_5_max.append(data["list"][38]["main"]["temp_max"])
day_5_max.append(data["list"][39]["main"]["temp_max"])

day_5_max_mean = statistics.mean(day_5_max)
day_5_max_mean = round(day_5_max_mean, ndigits = 2)

# creating the fifth day of the forecast humidity
day_5_hum = []

day_5_hum.append(data["list"][32]["main"]["humidity"])
day_5_hum.append(data["list"][33]["main"]["humidity"])
day_5_hum.append(data["list"][34]["main"]["humidity"])
day_5_hum.append(data["list"][35]["main"]["humidity"])
day_5_hum.append(data["list"][36]["main"]["humidity"])
day_5_hum.append(data["list"][37]["main"]["humidity"])
day_5_hum.append(data["list"][38]["main"]["humidity"])
day_5_hum.append(data["list"][39]["main"]["humidity"])

day_5_hum_mean = statistics.mean(day_5_hum)
day_5_hum_mean = round(day_5_hum_mean, ndigits = 2)

## Degree Symbol
degreeSym = chr(176)

# Printing the results in a readable format for the user.
print("\n")
print(f"The next five day forecast in {city} is:")
print("\n")
print("Tomorrow's weather is:")
print(f"The average minimum temperature will be: {day_1_min_mean}{degreeSym}F.")
print(f"The average maximum temperature will be: {day_1_max_mean}{degreeSym}F.")
print(f"The average humidity will be: {day_1_hum_mean}.")
print("\n")
print("Day 2's weather will be:")
print(f"The average minimum temperature will be: {day_2_min_mean}{degreeSym}F.")
print(f"The average maximum temperature will be: {day_2_max_mean}{degreeSym}F.")
print(f"The average humidity will be: {day_2_hum_mean}.")
print("\n")
print("Day 3's weather will be:")
print(f"The average minimum temperature will be: {day_3_min_mean}{degreeSym}F.")
print(f"The average maximum temperature will be: {day_3_max_mean}{degreeSym}F.")
print(f"The average humidity will be: {day_3_hum_mean}.")
print("\n")
print("Day 4's weather will be:")
print(f"The average minimum temperature will be: {day_4_min_mean}{degreeSym}F.")
print(f"The average maximum temperature will be: {day_4_max_mean}{degreeSym}F.")
print(f"The average humidity will be: {day_4_hum_mean}.")
print("\n")
print("Day 5's weather will be:")
print(f"The average minimum temperature will be: {day_5_min_mean}{degreeSym}F.")
print(f"The average maximum temperature will be: {day_5_max_mean}{degreeSym}F.")
print(f"The average humidity will be: {day_5_hum_mean}.")
print("\n")

## PUTTING DATA INTO DATAFRAME

data_frame = pd.DataFrame(list(zip(day_1_min, day_1_max, day_1_hum, day_2_min, day_2_max, day_2_hum, day_3_min, day_3_max, day_3_hum, day_4_min, day_4_max, day_4_hum, day_5_min, day_5_max, day_5_hum)), 
index = ['12 AM', '3 AM', '6 AM', '9 AM', '12 PM', '3 PM', '6 PM', '9 PM'], 
columns = ['Day 1 Min Temp', 'Day 1 Max Temp', 'Day 1 Humidity', 'Day 2 Min Temp', 'Day 2 Max Temp', 'Day 2 Humidity', 'Day 3 Min Temp', 'Day 3 Max Temp', 'Day 3 Humidity', 'Day 4 Min Temp', 'Day 4 Max Temp', 'Day 4 Humidity', 'Day 5 Min Temp', 'Day 5 Max Temp', 'Day 5 Humidity'])

data_frame.to_csv(r'~\Weather.csv', header = True)