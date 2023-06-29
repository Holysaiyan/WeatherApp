
WeatherApp

This module provides the WeatherApp class, which is a Python command-line application
for retrieving current weather information and weather forecasts using the OpenWeatherMap API.

The WeatherApp class allows users to interact with the application by providing options to
check the current weather for a specific location and to fetch weather forecasts for the next
few days.

Dependencies:
- requests: A Python library for making HTTP requests.
- python-dotenv: A Python library for managing environment variables.

Usage:
1. Instantiate the WeatherApp class.
2. Set up the required environment variables, including the OpenWeatherMap API key.
3. Use the available methods to fetch weather information.

-------------------------------------------------------------------------------
BEFORE YOU CAN USE THE APP

You will need to create a .env file (no extension). It has to be in the same directory as the program
<img width="434" alt="Screenshot 2023-06-28 114657" src="https://github.com/Holysaiyan/WeatherApp/assets/53127211/495d8290-a847-4dda-ac1e-63aba4db8028">

and write this code
<img width="308" alt="3" src="https://github.com/Holysaiyan/WeatherApp/assets/53127211/b99473fb-1618-4598-a236-e71c5beb48f4">

weather_api_key=YOUR_API_KEY_GOES_HERE

no need to put the api key in a string
-------------------------------------------------------------------------------


Example:
from WeatherApp import WeatherApp

Instantiate the WeatherApp class


weather_app = WeatherApp()

To Retrieve current weather for a specific location


current_weather = weather_app.current_weather("London")


print(current_weather)


To Fetch weather forecast for a specific location


forecast = weather_app.forecast_weather("Paris", 5)


print(forecast)


