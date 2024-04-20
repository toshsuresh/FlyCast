from flask import request, jsonify, render_template
from .model import predict_delay
from .webscrape import get_weather

# Ensure we're importing the correct functions
from flask import Blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    city = data['city']
    departure_time = data['departure_time']

    # Get weather data for the given city and departure time
    weather_data = get_weather(city, departure_time)

    if 'error' in weather_data:
        return jsonify({"error": weather_data['error']}), 400

    # Prepare features for prediction
    features = [weather_data['temperature'], weather_data['precipitation'], weather_data['pressure'], weather_data['visibility'], weather_data['wind_speed']]

    delay_minutes = predict_delay(features)
    return jsonify({"delayed_minutes": delay_minutes[0]})