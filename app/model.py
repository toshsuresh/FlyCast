import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load data
def load_data():
    data = pd.read_csv('path_to_your_csv/flight_weather_data.csv')
    return data

# Preprocess and split the data
def preprocess_data(data):
    # Fill missing values if any
    data = data.fillna(method='ffill')
    
    X = data[['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']]
    y = data['departure_delay']
    
    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Predict delay
def predict_delay(model, X):
    predicted_delay = model.predict(X)
    return predicted_delay

# Example usage in your app
data = load_data()
X_train, X_test, y_train, y_test = preprocess_data(data)
model = train_model(X_train, y_train)

# Now you can use 'model' to predict using new data processed similarly to X_test
