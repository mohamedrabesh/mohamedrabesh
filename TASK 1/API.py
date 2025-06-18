import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# OpenWeatherMap API Key (get your free key from https://openweathermap.org/api)
API_KEY = '496a84dcded04da4328e36a7f2b1d2bb'  # Replace with your API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# List of cities for data fetching
cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Bangalore']

# Lists to store fetched data
temperatures = []
humidities = []
pressures = []

for city in cities:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperatures.append(data['main']['temp'])
        humidities.append(data['main']['humidity'])
        pressures.append(data['main']['pressure'])
        print(f"Fetched data for {city}")
    else:
        print(f"Failed to fetch data for {city}: {data.get('message')}")

# Visualization 1: Temperature
plt.figure(figsize=(8,5))
sns.barplot(x=cities, y=temperatures, palette='coolwarm')
plt.title('City-wise Temperature (°C)')
plt.ylabel('Temperature (°C)')
plt.xlabel('City')
plt.show()

# Visualization 2: Humidity
plt.figure(figsize=(8,5))
sns.barplot(x=cities, y=humidities, palette='Blues')
plt.title('City-wise Humidity (%)')
plt.ylabel('Humidity (%)')
plt.xlabel('City')
plt.show()

# Visualization 3: Pressure
plt.figure(figsize=(8,5))
sns.barplot(x=cities, y=pressures, palette='Greens')
plt.title('City-wise Pressure (hPa)')
plt.ylabel('Pressure (hPa)')
plt.xlabel('City')
plt.show()
