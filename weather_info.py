# weather_info.py
# Author: Your Name
# Date: October 2025
# Description: A simple script that fetches current weather info for a city
# using the Open-Meteo API (no API key required). Great for Hacktoberfest! 🎃

import requests

def get_weather(city):
    """
    Fetches approximate current weather data for the given city using Open-Meteo.
    """
    # Simple city-to-coordinate mapping (for demo purposes)
    cities = {
        "london": (51.5072, -0.1276),
        "new york": (40.7128, -74.0060),
        "tokyo": (35.6762, 139.6503),
        "paris": (48.8566, 2.3522),
        "delhi": (28.6139, 77.2090)
    }

    city_key = city.lower()
    if city_key not in cities:
        return f"❌ Sorry, I don't have data for '{city}'. Try another city."

    lat, lon = cities[city_key]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        weather = data["current_weather"]
        return (
            f"🌤️ Weather in {city.title()}:\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Windspeed: {weather['windspeed']} km/h\n"
            f"Time: {weather['time']}"
        )
    except Exception as e:
        return f"⚠️ Error fetching weather: {e}"

def main():
    print("=== Simple Weather Info App ===")
    city = input("Enter a city (e.g., London, Tokyo): ")
    print(get_weather(city))

if __name__ == "__main__":
    main()
