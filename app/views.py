from flask import Blueprint, render_template, request, jsonify
from .model import model, predict_delay, preprocess_data  # Import necessary functions
import numpy as np  # Add this line to import NumPy

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert form data to correct format
        temperature = float(request.form['temperature'])
        precipitation = float(request.form['precipitation'])
        pressure = float(request.form['pressure'])
        visibility = float(request.form['visibility'])
        windspeed = float(request.form['windspeed'])
        
        # Create a numpy array of the input features
        features = np.array([[temperature, precipitation, pressure, visibility, windspeed]])
        predicted_minutes = predict_delay(model, features)
        
        return jsonify({"status": "success", "predicted_delay_minutes": predicted_minutes[0]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
