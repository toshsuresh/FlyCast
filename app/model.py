import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.preprocessing import StandardScaler  # Import StandardScaler

# Load data and train model
def load_and_train():
    # Get the path to the CSV file relative to the app directory
    csv_path = os.path.join(os.path.dirname(__file__), 'flight_weather_data.csv')

    # Load the data
    df = pd.read_csv(csv_path)
    features = df[['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']]
    target = df['departure_delay']

    # Normalize/scale the input features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)  # Adjust parameters
    model.fit(X_train, y_train)

    # Save the model to disk
    joblib.dump(model, 'flight_delay_predictor_model.pkl')

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)

# Function to predict delay
def predict_delay(features):
    # Load trained model from disk
    model = joblib.load('flight_delay_predictor_model.pkl')
    # Predict using the model
    predicted_delay = model.predict([features])
    return predicted_delay