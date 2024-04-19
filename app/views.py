from flask import Blueprint, render_template, request, jsonify
from .model import fetch_weather, predict_delay  # Import from model.py

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    flight_date = request.form['date']
    airport_code = request.form['flight_number']  # As a placeholder, eventually replace with actual airport code handling logic

    weather = fetch_weather(flight_date, airport_code)
    is_delayed = predict_delay(weather)
    return jsonify({"status": "success", "delayed": is_delayed})
