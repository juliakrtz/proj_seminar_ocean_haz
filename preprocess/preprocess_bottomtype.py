#importing bottom type API
import geopandas

#import requests

DB_SCHEMA = "sa"
TABLE = "bottom_type"
DOWNLOAD_DIR = "data/original"
PROCESSED_DIR = "data/processed"

url_bottom_type = "https://opendata.arcgis.com/datasets/4780150a51064c37bc627e2dcc4df615_2.geojson"

gdf_bottom_type = geopandas.read_file(url_bottom_type)




payload={}
headers = {
  'Authorization': '5b3ce3597851110001cf624827861a30001c4ea7ac1a9dabbe858ce2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)