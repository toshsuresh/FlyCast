from flask import Blueprint, render_template, request, jsonify
import numpy as np
import pickle

main = Blueprint('main', __name__)

# Load the model and scaler from the saved files
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        temperature = float(request.form['temperature'])
        precipitation = float(request.form['precipitation'])
        pressure = float(request.form['pressure'])
        visibility = float(request.form['visibility'])
        windspeed = float(request.form['windspeed'])
        
        # Create a feature array and scale it
        features = np.array([[temperature, precipitation, pressure, visibility, windspeed]])
        features_scaled = scaler.transform(features)
        
        # Predict delay using the scaled features
        predicted_delay = model.predict(features_scaled)[0]
        
        # Return the prediction result as JSON
        return jsonify({"status": "success", "predicted_delay_minutes": predicted_delay})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

