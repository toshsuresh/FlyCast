from flask import Blueprint, render_template, request, jsonify
from .model import fetch_weather, predict_delay, fetch_flight_data, prepare_features  # Import the prepare_features function

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    flight_date = request.form['date']
    flight_iata = request.form['flight_number']  # Assuming users enter IATA code

    weather = fetch_weather(flight_date, flight_iata)  # using city as proxy for airport
    flight_data = fetch_flight_data(flight_date, flight_iata)
    features = prepare_features(weather, flight_data)  # Prepare the combined features
    is_delayed = predict_delay(features)  # Pass the features dictionary
    return jsonify({"status": "success", "delayed": is_delayed})
