#import coral reef API
import requests

url = "https://geodata.hawaii.gov/arcgis/rest/services/CoastalMarine/MapServer/7/query?where=1%3D1&outFields=*&outSR=4326&f=jsonwhere=1%3D1&outFields=*&outSR=4326&f=json"

url_coral_reef = "https://opendata.arcgis.com/datasets/9229d814438349948c99b5e61a084418_7.geojson"


payload={}
headers = {
  'Authorization': '5b3ce3597851110001cf624827861a30001c4ea7ac1a9dabbe858ce2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
