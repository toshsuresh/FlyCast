# app/webscrape.py
import requests
from datetime import datetime, timezone
from geopy.geocoders import Nominatim

def get_weather(city, departure_time):
    departure_datetime = datetime.fromisoformat(departure_time).astimezone(timezone.utc)
    geolocator = Nominatim(user_agent="flight_delay_predictor")
    location = geolocator.geocode(city)
    if not location:
        return {"error": "City not found"}

    start_datetime = departure_datetime.isoformat(timespec='seconds') + 'Z'
    end_datetime = departure_datetime.isoformat(timespec='seconds') + 'Z'  # Consider adjusting if range needed

    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m,precipitation,pressure_msl,visibility,windspeed_10m&start={start_datetime}&end={end_datetime}"
    response = requests.get(url)
    data = response.json()

    if 'hourly' in data:
        weather_parameters = {
            'temperature': data['hourly']['temperature_2m'][0],
            'precipitation': data['hourly']['precipitation'][0],
            'pressure': data['hourly']['pressure_msl'][0],
            'visibility': data['hourly']['visibility'][0],
            'wind_speed': data['hourly']['windspeed_10m'][0]
        }
        print("Weather data fetched:", weather_parameters)  # Debugging output
        return weather_parameters
    else:
        return {"error": "Weather data not available"}
