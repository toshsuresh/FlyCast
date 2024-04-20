import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

def load_data(filepath='data/flight_weather_data.csv'):
    # Get the directory where this script resides
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # This points to '/workspaces/SkyCast'
    full_path = os.path.join(base_dir, filepath)  # Construct the full path to the CSV
    data = pd.read_csv(full_path)
    return data

def preprocess_and_split(data):
    # Handle missing values and scale the data
    data.fillna(0, inplace=True)
    X = data[['HourlyDryBulbTemperature_x', 'HourlyPrecipitation_x', 'HourlyStationPressure_x', 'HourlyVisibility_x', 'HourlyWindSpeed_x']]
    y = data['departure_delay']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42), scaler

def train_model(X_train, y_train):
    # Train a RandomForest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model_and_scaler(model, scaler, model_path='model.pkl', scaler_path='scaler.pkl'):
    # Get the directory where this script resides
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # This points to '/workspaces/SkyCast'
    full_model_path = os.path.join(base_dir, model_path)  # Save in the root directory
    full_scaler_path = os.path.join(base_dir, scaler_path)  # Save in the root directory

    with open(full_model_path, 'wb') as f:
        pickle.dump(model, f)
    with open(full_scaler_path, 'wb') as f:
        pickle.dump(scaler, f)

# This block is at the end of your model.py
if __name__ == "__main__":
    data = load_data()
    (X_train, X_test, y_train, y_test), scaler = preprocess_and_split(data)
    model = train_model(X_train, y_train)
    save_model_and_scaler(model, scaler)
