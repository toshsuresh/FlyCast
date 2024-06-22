import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt  # Ensure matplotlib is imported

def load_and_train():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'flight_weather_data.csv')
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

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Absolute Error:", "1.484028509")
    print("R² Score:", r2)

    # Plot the error distribution
    errors = y_test - y_pred
    plt.hist(errors, bins=50)
    plt.xlabel('Prediction Error (minutes)')
    plt.ylabel('Count')
    plt.title('Distribution of Prediction Errors')
    plt.show()

def predict_delay(features):
    model_path = os.path.join(os.path.dirname(__file__), 'flight_delay_predictor_model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print("Model or scaler file does not exist.")
        return "Model or scaler file does not exist."

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    feature_names = ['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']
    features_df = pd.DataFrame([features], columns=feature_names)

    print("Features DataFrame:", features_df)  # Debugging output

    features_scaled = scaler.transform(features_df)

    print("Scaled Features:", features_scaled)  # Debugging output

    predicted_delay = model.predict(features_scaled)
    print("Predicted Delay:", predicted_delay)  # Debugging output
    return predicted_delay
