import requests
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv('.env')

# Get the API key from the environment variable
# api_key ='d88f2005973a1a84fb6f5f92ddf4b943'
api_key = os.getenv('OpenWeatherMapAPIKey')

# Define the API endpoint URL
location = input("Nhap ten thanh pho: ")
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Hanoi&appid={api_key}&units=metric")
response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the weather data from the response
    geo_data = response.json()
    print(geo_data)
else:
    print("Error: Failed to retrieve weather data")
    print(response.json())

# Get lat, lon of the city
geo_data
print(type(geo_data))
geo_data[0]
lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]
lat, lon

# Define the API endpoint URL
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Hanoi&appid={api_key}&units=metric")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the weather data from the response
    weather_data = response.json()
    # weather_data
else:
    print("Error: Failed to retrieve weather data")
    print(response.json())


# Print request info:
print(f"""Location {weather_data["name"]}
Nhiet do {weather_data["main"]['feels_like']}
Tam nhin {weather_data["visibility"]}
""")
