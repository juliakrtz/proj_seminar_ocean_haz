import arrow
import requests

def get_weather(x,y): ##note: to get weather API data, will need a stormglass account and login to get the key. It is free. 
 # API_key = "389b62d8-8758-11ec-8bae-0242ac130002-389b6350-8758-11ec-8bae-0242ac130002" #julia's key
 # API_key = "23bd5da0-8f49-11ec-a301-0242ac130002-23bd5e18-8f49-11ec-a301-0242ac130002" #paula's key
  API_key = "58e57908-94a4-11ec-8cc9-0242ac130002-58e5798a-94a4-11ec-8cc9-0242ac130002" #paula's key n2

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
