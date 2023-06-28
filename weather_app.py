"""
WeatherApp Module
A simple weather application for retrieving current weather and
weather forecast data using the WeatherAPI.
"""
import os
import requests
from dotenv import load_dotenv


class WeatherApp:
    """
    A simple weather application for retrieving current weather
    and weather forecast data using the WeatherAPI.

    Attributes:
        _api_key (str): API key for accessing the WeatherAPI.

    """

    def __init__(self):
        """
        Initialize the WeatherApp instance.
        """
        self.configure()
        self._api_key = os.getenv('weather_api_key')

    def configure(self):
        """
        Load the environment variables from the .env file.
        """
        load_dotenv()

    def get_api(self):
        """
        Get the API key for accessing the WeatherAPI.

        Returns:
            str: The API key.
        """
        return self._api_key

    def current_weather(self):
        """
        Retrieve the current weather data for a given location.

        Returns:
            str: A formatted string with the current weather information for the specified location.

        """
        location = input("Enter Location: ")

        url = f"http://api.weatherapi.com/v1/current.json?key={self.get_api()}&q={location}"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()

            country_name = weather_data['location']['country']
            country_region = weather_data['location']['region']
            current_temp = weather_data['current']['temp_c']
            current_time = weather_data['current']['last_updated']
            current_weather_condition = weather_data["current"]["condition"]["text"]

            result = f"Hi there\n{location} is located in {country_name}, " \
                     f"in the {country_region} region.\nThe " \
                     f"current temperature is {current_temp}\u00b0C, " \
                     f"the weather condition is {current_weather_condition}." \
                     f" Weather information was last updated {current_time}"

            return result
        return "Api not found"

    def forecast_weather(self) -> str or None:
        """
        Retrieve the weather forecast for a given location and number of days.

        Returns:
            str: A formatted string with the weather forecast
            for the specified location and number of days.

        """
        location = input("Enter Location here: ")
        days = input("How many days you want the weather forecast for: ")
        unit_of_measurement = int(input("Enter 1 if you would like"
                                        " the unit of measurement in Celsius,\nor "
                                        "Enter 2 if you would like in "
                                        "Fahrenheit "))
        url = f"http://api.weatherapi.com/v1/forecast.json?key=" \
              f"{self.get_api()}&q={location}&days={days}"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            forecast = weather_data['forecast']['forecastday']
            location_name = weather_data['location']['name']
            location_country = weather_data['location']['country']

            forecast_data = []
            result = ""
            for day in forecast:
                date = day['date']
                max_temp_c = day['day']['maxtemp_c']
                min_temp_c = day['day']['mintemp_c']
                max_temp_f = day['day']['maxtemp_f']
                min_temp_f = day['day']['mintemp_f']
                condition = day['day']['condition']['text']
                forecast_data.append({'date': date, 'max_temp': max_temp_c,
                                      'min_temp': min_temp_c, 'condition':
                                     condition})
                if unit_of_measurement == 1:
                    result += f"On {date}, the weather forecast for {location_name} in" \
                              f" {location_country} predicts {condition}," \
                              f" the highest temperature will be {max_temp_c}\u00b0C," \
                              f" and the lowest will be {min_temp_c}\u00b0C\n\n"
                elif unit_of_measurement == 2:
                    result += f"On {date}, the weather forecast for {location_name} in" \
                              f" {location_country} predicts {condition}," \
                              f" the highest temperature will be {max_temp_f}\u00b0F," \
                              f" and the lowest will be {min_temp_f}\u00b0F\n\n"
                else:
                    return "Invalid input"
            return result

        print("Error fetching weather forecast data:", response.text)
        return None
