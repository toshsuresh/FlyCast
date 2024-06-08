import requests
from datetime import datetime, timezone, timedelta
from geopy.geocoders import Nominatim

def get_weather(city, departure_time):
    departure_datetime = datetime.fromisoformat(departure_time).astimezone(timezone.utc)
    geolocator = Nominatim(user_agent="flight_delay_predictor")
    location = geolocator.geocode(city)
    if not location:
        print(f"City not found: {city}")
        return {"error": "City not found"}

    start_datetime = departure_datetime.isoformat(timespec='seconds') + 'Z'
    end_datetime = (departure_datetime + timedelta(hours=1)).isoformat(timespec='seconds') + 'Z'

    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m,precipitation,pressure_msl,visibility,windspeed_10m&start={start_datetime}&end={end_datetime}"
    response = requests.get(url)
    data = response.json()

    print("Full weather data response:", data)  # Debugging output

    if 'hourly' in data and 'temperature_2m' in data['hourly']:
        hours = data['hourly']['time']
        
        # Convert all times to aware datetime objects
        hours_aware = [datetime.fromisoformat(hour).replace(tzinfo=timezone.utc) for hour in hours]
        
        closest_time = min(hours_aware, key=lambda x: abs(x - departure_datetime))

        index = hours_aware.index(closest_time)
        weather_parameters = {
            'temperature': data['hourly']['temperature_2m'][index],
            'precipitation': data['hourly']['precipitation'][index],
            'pressure': data['hourly']['pressure_msl'][index],
            'visibility': data['hourly']['visibility'][index],
            'wind_speed': data['hourly']['windspeed_10m'][index]
        }
        print("Weather data fetched:", weather_parameters)  # Debugging output
        return weather_parameters
    else:
        print("Weather data not available or missing keys in response")
        return {"error": "Weather data not available"}