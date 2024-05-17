# SkyCast: Flight Delay Predictor

SkyCast is an innovative Flask application designed to predict flight delays by analyzing real-time weather data. This application utilizes machine learning models trained on historical flight and weather data to provide accurate predictions of potential delays based on weather conditions such as temperature, precipitation, pressure, visibility, and wind speed.

## Features

- **Weather Data Integration**: Fetches live weather data using the Open-Meteo API based on the city and scheduled departure time.
- **Machine Learning Prediction**: Utilizes a RandomForest model to predict flight delays based on processed weather conditions.
- **User-Friendly Web Interface**: Easy-to-use web interface for inputting flight details and receiving delay predictions.
- **Data Scalability**: Designed to handle and scale with extensive flight and weather datasets.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- Pip for package installation

## Installation

To set up SkyCast locally, follow these steps:

1. Clone the repository:
git clone https://github.com/yourusername/SkyCast.git
cd SkyCast


2. Install the required packages:
pip install -r requirements.txt

3. Initialize the application:
python -m app

## Usage

To use SkyCast, start the Flask server:
python -m app

Navigate to `http://localhost:5000` in your web browser. Enter the city and departure time of the flight to receive the delay prediction.

## How It Works

1. **Data Collection**: The application first collects historical flight and weather data stored in `flight_weather_data.csv`.
2. **Model Training**: The data is processed and used to train a RandomForestRegressor. This model along with a StandardScaler is then saved for future predictions.
3. **Weather Data Fetching**: At runtime, the application uses the Open-Meteo API to fetch real-time weather data based on user input.
4. **Delay Prediction**: The fetched weather data is processed and fed into the trained model to predict potential flight delays.

## Contributing

Contributions to SkyCast are welcome!

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
