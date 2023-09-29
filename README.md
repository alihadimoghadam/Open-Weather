# Open Weather
This Python application allows users to check the current weather in various capital cities around the world. It utilizes the OpenWeatherMap API to fetch real-time weather data. Users can input a capital city name, click the "Get Weather" button, and receive information about the temperature and weather description for the specified city. Additionally, the weather data is saved to a CSV file along with a timestamp for future reference.

# Installation
1. Clone the Repository:
`git clone https://github.com/alihadimoghadam/Open-Weather.git`

2. Navigate to the Project Directory:
`cd Open-Weather`

3. Install the Dependecies:
`pip install requests`

# Usage
1. Run the Application:
`python main.py`

2. Enter a Capital City:
Type the name of a capital city in the input field.

3. Get Weather Information:
Click the "Get Weather" button to fetch and display the current weather information for the specified city

4. Check Saved Weather Data:
The weather data for each query is saved in a CSV file named 'weather_data.csv' along with a timestamp. You can find this file in the project directory.

# API Key
To fetch weather data, the application uses the OpenWeatherMap API. You need to replace '-----' in the code with your valid OpenWeatherMap API key. You can obtain a free API key by signing up on the OpenWeatherMap website.

# Notes
The application provides weather information for a predefined list of capital cities. You can add more cities to the capital_cities dictionary in the code if needed.

Weather data is displayed in Celsius by default. You can change the units to Fahrenheit by modifying the units parameter in the get_weather_data function.

In case of an error or if the specified city is not in the list of capital cities, an appropriate message will be displayed to the user.

# License

[MIT License](LICENSE)

Feel free to customize the README file according to your specific project requirements and any additional information you would like to provide to users.