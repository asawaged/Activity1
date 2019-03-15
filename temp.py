from datetime import datetime
import requests
import pytemperature


now = datetime.now()

print("ISQA 3900 Open Weather API")

print()
choice = "y"
while choice.lower() == "y":
    city = input("Enter city:     ")
    print("Use ISO letter country code like: https://countrycode.org/")
    country = input("Enter country code:     ")

    api_start = 'https://api.openweathermap.org/data/2.5/weather?q= '


    api_key = '&appid=48e2f5fc16f340549f59f9ab43e38690'


    url = api_start + city + ',' + country + api_key

    json_data = requests.get(url).json()
    weather_description = json_data['weather'][0]['description']
    temp= json_data ['main']['temp']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    low = json_data['main']['temp_min']
    high = json_data['main']['temp_max']


    print("Current conditions:  ", weather_description)
    print("Current Temperature in Fahrenheit:  ",pytemperature.k2f(temp) )
    print("Current pressure in inHG: ",round(pressure * 0.0295300,2 ))
    print("Current % Humidity: ",humidity)
    print("Expected low temperature in Fahrenheit: ",pytemperature.k2f(low))
    print("Expected high temperature in fahrenheit: ",pytemperature.k2f(high))







    choice = input("Continue (y/n)?: ")
    print()
print('Bye')
