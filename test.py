import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the weather API key from the environment variable
api_key = os.getenv('weather_api_key')

# Print the value of the API key to verify if it's retrieved correctly
print(api_key)
