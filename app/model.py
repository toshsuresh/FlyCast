import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

def load_data(filepath):
    # Load the dataset
    data = pd.read_csv(filepath)
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
    # Save the trained model and scaler for later use
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)

# This block is used to prepare the model initially
if __name__ == "__main__":
    data = load_data('path_to_your_csv_file.csv')
    (X_train, X_test, y_train, y_test), scaler = preprocess_and_split(data)
    model = train_model(X_train, y_train)
    save_model_and_scaler(model, scaler)
