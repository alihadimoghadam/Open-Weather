import requests
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

API_KEY = '-----'

# Dictionary of capital cities with their corresponding city names
capital_cities = {
    'Amsterdam': 'Amsterdam,nl',
    'Athens': 'Athens,gr',
    'Bangkok': 'Bangkok,th',
    'Beijing': 'Beijing,cn',
    'Brasília': 'Brasilia,br',
    'Cairo': 'Cairo,eg',
    'Canberra': 'Canberra,au',
    'Copenhagen': 'Copenhagen,dk',
    'Dublin': 'Dublin,ie',
    'Helsinki': 'Helsinki,fi',
    'Islamabad': 'Islamabad,pk',
    'Kiev': 'Kiev,ua',
    'Lisbon': 'Lisbon,pt',
    'Madrid': 'Madrid,es',
    'Mexico City': 'Mexico City,mx',
    'Moscow': 'Moscow,ru',
    'Nairobi': 'Nairobi,ke',
    'New Delhi': 'New Delhi,in',
    'Oslo': 'Oslo,no',
    'Ottawa': 'Ottawa,ca',
    'Rome': 'Rome,it',
    'Seoul': 'Seoul,kr',
    'Stockholm': 'Stockholm,se',
    'Vienna': 'Vienna,at',
    'Warsaw': 'Warsaw,pl',
    'Washington, D.C.': 'Washington,us',
    'London': 'London,uk',
    'Paris': 'Paris,fr',
    'Berlin': 'Berlin,de',
    'Tokyo': 'Tokyo,jp',
    # Add more capital cities here
}

# Function to fetch weather data for a city
def get_weather_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

# Function to handle button click
def get_weather_info():
    city_name = city_entry.get()
    city_name = city_name.strip()
    
    if city_name in capital_cities:
        city_id = capital_cities[city_name]
        weather_data = get_weather_data(city_id)
    
        if weather_data:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            result_label.config(text=f"Weather in {city_name}:\nTemperature: {temperature}°C\nDescription: {description}")
            
            # Save weather data to a CSV file with a timestamp
            save_weather_to_csv(city_name, temperature, description)
        else:
            result_label.config(text=f"Failed to fetch weather data for {city_name}.")
    else:
        result_label.config(text=f"City not found in the list of capital cities.")

# Function to save weather data to a CSV file with a timestamp
def save_weather_to_csv(city_name, temperature, description):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('weather_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([city_name, temperature, description, timestamp])

# Create the main application window
app = tk.Tk()
app.title("Capital City Weather")

# Create and configure widgets
city_label = tk.Label(app, text="Enter a capital city:")
city_entry = tk.Entry(app)
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_info)
result_label = tk.Label(app, text="", wraplength=300, justify='left')

# Place widgets in the window
city_label.pack(pady=5)
city_entry.pack(pady=5)
get_weather_button.pack(pady=5)
result_label.pack(pady=10)

# Start the GUI event loop
app.mainloop()
