import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib

def load_and_train():
    csv_path = os.path.join(os.path.dirname(__file__), 'flight_weather_data.csv')
    df = pd.read_csv(csv_path)
    features = df[['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']]
    target = df['departure_delay']

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, os.path.join(os.path.dirname(__file__), 'flight_delay_predictor_model.pkl'))
    joblib.dump(scaler, os.path.join(os.path.dirname(__file__), 'scaler.pkl'))

    mse = mean_squared_error(y_test, model.predict(X_test))
    print("Mean Squared Error:", mse)

def predict_delay(features):
    model_path = os.path.join(os.path.dirname(__file__), 'flight_delay_predictor_model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        return "Model or scaler file does not exist."

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Ensure feature names match training data
    feature_names = ['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']
    features_df = pd.DataFrame([features], columns=feature_names)

    # Scale features
    features_scaled = scaler.transform(features_df)
    
    predicted_delay = model.predict(features_scaled)
    return predicted_delay
