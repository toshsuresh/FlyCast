
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
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
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

## Contact

For any inquiries or feedback, please reach out to us at [akhil.metukuru2016@gmail.com].

---

Thank you for using SkyCast! We hope it provides valuable insights for your flight planning needs.
```
