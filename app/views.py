from flask import Blueprint, render_template, request, jsonify
import numpy as np
import pickle

main = Blueprint('main', __name__)

# Set the base directory to point to the SkyCast directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths for model and scaler
model_path = os.path.join(base_dir, 'model.pkl')
scaler_path = os.path.join(base_dir, 'scaler.pkl')

# Function to load model and scaler
def load_model_scaler():
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, 'rb') as scaler_file:
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
        # It's good practice to log the actual error also
        print("An error occurred:", str(e))
        return jsonify({"status": "error", "message": "An error occurred during processing."})

