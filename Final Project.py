#EPSY 5200 Final Project Python Script File
#Author: Robert T. Kreml

Version = "0.0.1"
Date = "December 4, 2019"

print(f"Thank you for running this script! This is in partial fulfillment of the requirements for EPSY 5200 for the Fall 2019 Semester.")
print(f"You are currently running version: {Version}, created on: {Date}.")

import urllib.request
import urllib.parse
import json

city = input("Please type in the city you would like to get the weather for: ")

params = {"appid":"7d8615fc2e5e528e24c0a03e480f10e1", "q": city, "units": "imperial"}
arguments = urllib.parse.urlencode(params)

address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

webData = urllib.request.urlopen(url)
results = webData.read().decode('UTF-8')
webData.close()

data = json.loads(results)

current = data["main"]
degreeSym = chr(176)

print(f"The current weather in {city} is the following:")
print(f'The current temperature: {current["temp"]}{degreeSym}F')
print(f"The minimum temperature today in {city} is: {current['temp_min']}{degreeSym}F")
print(f"The high temperature today in {city} is: {current['temp_max']}{degreeSym}F")
print(f'{city} is currently experiencing {current["humidity"]}% humidity')