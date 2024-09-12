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
=======

# SkyCast: Flight Delay Predictor

**Technologies Used:** Flask, React, Pandas, Scikit-Learn

## Project Overview

SkyCast is a sophisticated application designed to predict flight delays by analyzing real-time weather metrics. By leveraging the Open-Meteo API, the application provides accurate and timely predictions, ensuring that users are well-informed about potential delays. The project combines a robust Flask backend with an interactive React frontend, delivering a seamless user experience.

## Features

- **Real-time Weather Analysis:** 
  - The application fetches and analyzes five critical weather metrics: temperature, precipitation, wind speed, pressure, and visibility.
- **Machine Learning Model:**
  - A RandomForestRegressor model was engineered to predict flight delays, achieving an impressive mean absolute error (MAE) of 1.48 minutes.
- **Scalable React Interface:**
  - Designed a dynamic and user-friendly React interface for seamless interaction.
  - Integrated with a Flask backend to handle over 33,000 API calls daily, ensuring robustness and efficient traffic management.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/skycast-flight-delay-predictor.git
   cd skycast-flight-delay-predictor
   ```

2. **Backend Setup:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the Flask server:
     ```bash
     flask run
     ```

3. **Frontend Setup:**
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

## Usage

1. Open your web browser and go to `http://localhost:3000` to interact with the application.
2. Input the required weather metrics to get predictions for flight delays.

## Contributing

We welcome contributions to SkyCast! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. **Fork the Repository**
2. **Create your Feature Branch (`git checkout -b feature/AmazingFeature`)**
3. **Commit your Changes (`git commit -m 'Add some AmazingFeature'`)**
4. **Push to the Branch (`git push origin feature/AmazingFeature`)**
5. **Open a Pull Request**

## License

This project is licensed under the MIT License.
---
