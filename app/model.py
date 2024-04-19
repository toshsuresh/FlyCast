import requests
from datetime import datetime

# Dummy function to fetch weather data
def fetch_weather(date, airport_code):
    # This is a placeholder; you need to use your actual API key and handle real data correctly.
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': 'your_api_key',  # Replace 'your_api_key' with the actual key.
        'dt': int(datetime.strptime(date, "%Y-%m-%d").timestamp()),
        'units': 'metric',
        'q': airport_code  # Assuming airport_code is city name
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # JSON response
    else:
        return None
    
def fetch_flight_data(flight_date, flight_iata):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        'access_key': 'b3270119e2d16c6e1f317872745fd8ee',  # Your actual API key
        'flight_iata': flight_iata,
        'flight_date': flight_date
    }
    response = requests.get(url, params=params)
    flight_info = response.json()
    print(flight_info)  # Print the entire API response
    if 'error' in flight_info:
        # Handle error response from API
        error_message = flight_info['error'].get('info', 'Unknown error occurred')
        print("Error:", error_message)
        return None
    else:
        # Process the flight_info as needed for your prediction model
        return flight_info



def prepare_features(weather_data, flight_data):
    features = {}
    if weather_data:
        features['temp'] = weather_data['main']['temp']
        features['condition'] = weather_data['weather'][0]['main']  # 'Rain', 'Clear', etc.
    if flight_data and 'data' in flight_data and len(flight_data['data']) > 0:
        # Assuming the API returns whether the last flight was delayed
        features['recent_delay'] = flight_data['data'][0]['delay'] > 0
    return features

def predict_delay(features):
    # Simple rules based on new features
    if features.get('temp', 10) < 0 or features.get('condition') in ['Snow', 'Rain']:
        return True
    elif features.get('recent_delay', False):
        return True
    return False