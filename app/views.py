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
        return jsonify({"error": weather_data['error']}), 400

    # Ensure the features are correctly named and ordered
    features = [
        weather_data['temperature'],
        weather_data['precipitation'],
        weather_data['pressure'],
        weather_data['visibility'],
        weather_data['wind_speed']
    ]

    # Call predict_delay with the correct features
    delay_minutes = predict_delay(features)
    return jsonify({"delayed_minutes": delay_minutes[0]})
