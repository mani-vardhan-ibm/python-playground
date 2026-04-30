# Weather App

A simple command-line weather application that fetches real-time weather data using the **Open-Meteo** free API (no API key required).

## Features

- Geocoding: resolve a city name to coordinates
- Current weather: temperature, humidity, wind speed, and condition
- Works with any city in the world

## Usage

```bash
# From repo root
python apps/01-weather-app/app.py London

# Or run interactively
python apps/01-weather-app/app.py
```

## Example Output

```
========================================
  Weather in London
========================================
  Condition    : Partly cloudy
  Temperature  : 14.2 °C
  Humidity     : 72 %
  Wind Speed   : 18.5 km/h
========================================
```

## API

Uses the free [Open-Meteo](https://open-meteo.com/) API – no registration or API key needed.
