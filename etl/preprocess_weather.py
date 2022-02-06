#import weather data, will change by coordinate
import requests

url = "https://api.stormglass.io/v2/weather/point"

payload={}
headers = {
  'Authorization': '5b3ce3597851110001cf624827861a30001c4ea7ac1a9dabbe858ce2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
