"""
App 01 – Weather App
---------------------
Fetches current weather data for a city using the Open-Meteo free API
(no API key required).

Usage:
    python app.py [city]

Example:
    python app.py London
"""

import sys
import urllib.request
import urllib.parse
import urllib.error
import json

# Geocoding API (free, no key)
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
# Weather API (free, no key)
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city: str) -> tuple[float, float, str]:
    """Return (latitude, longitude, resolved_name) for a city name."""
    params = urllib.parse.urlencode({"name": city, "count": 1, "language": "en", "format": "json"})
    with urllib.request.urlopen(f"{GEO_URL}?{params}") as response:
        data = json.loads(response.read())

    if not data.get("results"):
        raise ValueError(f"City '{city}' not found.")

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]


def get_weather(lat: float, lon: float) -> dict:
    """Return current weather data for the given coordinates."""
    params = urllib.parse.urlencode({
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weathercode",
        "wind_speed_unit": "kmh",
    })
    with urllib.request.urlopen(f"{WEATHER_URL}?{params}") as response:
        return json.loads(response.read())


def display_weather(city: str, weather: dict) -> None:
    """Print a formatted weather report."""
    current = weather["current"]
    code = current.get("weathercode", -1)
    condition = WMO_CODES.get(code, "Unknown")

    print("\n" + "=" * 40)
    print(f"  Weather in {city}")
    print("=" * 40)
    print(f"  Condition    : {condition}")
    print(f"  Temperature  : {current['temperature_2m']} °C")
    print(f"  Humidity     : {current['relative_humidity_2m']} %")
    print(f"  Wind Speed   : {current['wind_speed_10m']} km/h")
    print("=" * 40 + "\n")


def main():
    city = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter city name: ").strip()
    if not city:
        print("Error: Please provide a city name.")
        sys.exit(1)

    try:
        lat, lon, resolved = get_coordinates(city)
        weather = get_weather(lat, lon)
        display_weather(resolved, weather)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        print(f"Network or data error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
