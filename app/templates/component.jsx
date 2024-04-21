import React, { useState } from 'react';

export default function Component() {
    const [city, setCity] = useState('');
    const [departureTime, setDepartureTime] = useState('');
    const [result, setResult] = useState('');

    const handleCityChange = (event) => {
        setCity(event.target.value);
    };

    const handleDepartureTimeChange = (event) => {
        setDepartureTime(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ city, departure_time: departureTime })
            });
            const data = await response.json();
            const prediction = parseFloat(data.delayed_minutes).toFixed(2); // Truncate and round to 2 decimal places
            setResult(`Prediction: ${prediction} minutes delay`);
        } catch (error) {
            console.error('Error:', error);
            setResult('Failed to predict the delay. Please try again.');
        }
    };

    return (
        <div>
            <h1>Check if your flight will be delayed</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="city">City:</label>
                <input
                    type="text"
                    id="city"
                    name="city"
                    value={city}
                    onChange={handleCityChange}
                    required
                /><br/><br/>
                <label htmlFor="departure_time">Departure Time:</label>
                <input
                    type="datetime-local"
                    id="departure_time"
                    name="departure_time"
                    value={departureTime}
                    onChange={handleDepartureTimeChange}
                    required
                /><br/><br/>
                <input type="submit" value="Predict Delay" />
            </form>
            <div>{result}</div>
            <div className="image-container">
                <img src="https://source.unsplash.com/random/800x600?airplane" alt="Airplane" />
                <img src="https://source.unsplash.com/random/800x600?weather" alt="Weather" />
                <img src="https://source.unsplash.com/random/800x600?clock" alt="Clock" />
            </div>
        </div>
    );
}
