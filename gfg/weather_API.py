import arrow
import requests

def get_weather(x,y):
  API_key = "23bd5da0-8f49-11ec-a301-0242ac130002-23bd5e18-8f49-11ec-a301-0242ac130002"

  # Get first hour of today
  start = arrow.now().floor('hour')

  # Get last hour of today
  end = arrow.now().ceil('hour')

  response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
      'lat': y,
      'lng': x,
      'params': ','.join(['waveHeight', 'waveDirection', 'windDirection', 'windSpeed']),
      'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
      'end': end.to('UTC').timestamp(),  # Convert to UTC timestamp
      'source': 'noaa'
    },
    headers={
      'Authorization': API_key
    }
  )
  weather_data = response.json()
  return weather_data
