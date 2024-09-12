from flask import Blueprint, request, jsonify, render_template
from .model import predict_delay
from .webscrape import get_weather

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    city = data['city']
    departure_time = data['departure_time']
    
    weather_data = get_weather(city, departure_time)
    if 'error' in weather_data:
        print(f"Error fetching weather data: {weather_data['error']}")
        return jsonify({"error": weather_data['error']}), 400

    features = [
        weather_data['temperature'],
        weather_data['precipitation'],
        weather_data['pressure'],
        weather_data['visibility'],
        weather_data['wind_speed']
    ]

    try:
        delay_minutes = predict_delay(features)
        return jsonify({"delayed_minutes": delay_minutes[0]})
    except Exception as e:
        print(f"Error predicting delay: {str(e)}")
        return jsonify({"error": "Failed to predict the delay. Please try again."}), 500