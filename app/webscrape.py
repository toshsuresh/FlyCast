import requests
from datetime import datetime, timezone
from geopy.geocoders import Nominatim

def get_weather(city, departure_time):
    # Convert departure_time to a datetime object
    departure_datetime = datetime.fromisoformat(departure_time).astimezone(timezone.utc)

    # Convert city to latitude and longitude using geopy
    geolocator = Nominatim(user_agent="flight_delay_predictor")
    location = geolocator.geocode(city)
    if location:
        latitude = location.latitude
        longitude = location.longitude
    else:
        # Handle the case when the city is not found
        return {"error": "City not found"}

    # Build the request URL
    start_datetime = departure_datetime.isoformat(timespec='seconds') + 'Z'
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation,pressure_msl,visibility,windspeed_10m&start={start_datetime}&end={start_datetime}"

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Extract weather parameters
    weather_parameters = {
        'temperature': data['hourly']['temperature_2m'][0],
        'precipitation': data['hourly']['precipitation'][0],
        'pressure': data['hourly']['pressure_msl'][0],
        'visibility': data['hourly']['visibility'][0],
        'wind_speed': data['hourly']['windspeed_10m'][0]
    }
    return weather_parameters