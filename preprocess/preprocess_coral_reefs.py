#import coral reef API
import geopandas

DB_SCHEMA = "sa"
TABLE = "bottom_type"
DOWNLOAD_DIR = "data/original"
PROCESSED_DIR = "data/processed"

url_coral_reef = "https://opendata.arcgis.com/datasets/9229d814438349948c99b5e61a084418_7.geojson"

gdf = geopandas.read_file(url_coral_reef)


payload={}
headers = {
  'Authorization': '5b3ce3597851110001cf624827861a30001c4ea7ac1a9dabbe858ce2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
