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
     setResult(`Prediction: ${data.delayed_minutes} minutes delay`);
   } catch (error) {
     console.error('Error:', error);
     setResult('Failed to predict the delay. Please try again.');
   }
 };

 return (
   <div key="1" className="flex flex-col min-h-screen">
     <header className="bg-gray-900 text-white py-4 px-6">
       <div className="container mx-auto flex justify-between items-center">
         <h1 className="text-2xl font-bold">Flight Delay Predictor</h1>
         <nav>
           <ul className="flex space-x-4">
             <li><a className="hover:text-gray-400" href="#">Home</a></li>
             <li><a className="hover:text-gray-400" href="#">Predict</a></li>
             <li><a className="hover:text-gray-400" href="#">About</a></li>
             <li><a className="hover:text-gray-400" href="#">Contact</a></li>
           </ul>
         </nav>
       </div>
     </header>
     <main className="flex-1 bg-gray-100 py-12">
       <div className="container mx-auto px-6">
         <section className="bg-white shadow-lg rounded-lg p-8 mb-8">
           <h2 className="text-2xl font-bold mb-4">Predict Flight Delay</h2>
           <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-6">
             <div className="space-y-2 col-span-2">
               <div>
                 <label className="block font-medium" htmlFor="city">City:</label>
                 <input
                   className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                   id="city"
                   type="text"
                   value={city}
                   onChange={handleCityChange}
                 />
               </div>
               <div>
                 <label className="block font-medium" htmlFor="departure_time">Departure Time:</label>
                 <input
                   className="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                   id="departure_time"
                   type="datetime-local"
                   value={departureTime}
                   onChange={handleDepartureTimeChange}
                 />
               </div>
               <button
                 className="col-span-2 bg-indigo-600 text-white font-medium py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50"
                 type="submit"
               >
                 Predict Delay
               </button>
               <div className="col-span-2 text-center">
                 {result}
               </div>
             </div>
           </form>
         </section>
       </div>
     </main>
     <footer className="bg-gray-900 text-white py-6">
       <div className="container mx-auto px-6 flex justify-between items-center">
         <p>© 2023 Flight Delay Predictor. All rights reserved.</p>
         <nav>
           <ul className="flex space-x-4">
             <li><a className="hover:text-gray-400" href="#">Privacy Policy</a></li>
             <li><a className="hover:text-gray-400" href="#">Terms of Service</a></li>
           </ul>
         </nav>
       </div>
     </footer>
   </div>
 );
}