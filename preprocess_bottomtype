#importing bottom type API
import requests

url = "https://geodata.hawaii.gov/arcgis/rest/services/CoastalMarine/MapServer/2/query?where=1%3D1&outFields=*&outSR=4326&f=json"

payload={}
headers = {
  'Authorization': '5b3ce3597851110001cf624827861a30001c4ea7ac1a9dabbe858ce2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
