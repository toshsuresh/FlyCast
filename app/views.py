from flask import Blueprint, render_template, request, jsonify
from .model import predict_delay  # Ensure we're importing the correct functions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    temperature = request.form['temperature']
    precipitation = request.form['precipitation']
    pressure = request.form['pressure']
    visibility = request.form['visibility']
    windspeed = request.form['windspeed']

    # Convert data to floats and create a features list
    features = [float(temperature), float(precipitation), float(pressure), float(visibility), float(windspeed)]
    
    # Predict delay
    delay_minutes = predict_delay(features)
    
    # Return the result
    return jsonify({"status": "success", "delayed_minutes": delay_minutes[0]})
