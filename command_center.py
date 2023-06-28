from weather_app import WeatherApp


def help_menu() -> str:
    """
    This displays the help menu
    :return: The help menu as a string.
    """
    result = "Help Menu\n"
    result += "Choose the following options\n"
    result += "1. Check current weather in a location\n"
    result += "2. Check weather forecast in a location, Enter location and days to forecast\n"
    result += "3. Help Menu\n"
    result += "4. Quit App\n"

    return result


def command_list(command):
    """
    Executes a command based on the user's input.
    :param command: The command to execute.
    :return: The result of the executed command.
    """
    funct_list = {"1": WeatherApp().current_weather,
                  "2": WeatherApp().forecast_weather,
                  "3": help_menu
                  }

    return funct_list[command]()
