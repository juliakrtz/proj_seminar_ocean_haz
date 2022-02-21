#import
import geopandas
import pandas
from sqlalchemy import create_engine
import pyproj 

#pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  

#set the table name in the database
TABLE = "coral_reefs"

#url where is located the geojson file
url_coral_reef = "https://opendata.arcgis.com/datasets/9229d814438349948c99b5e61a084418_7.geojson"

#convert the geojson file to geodataframe
gdf = geopandas.read_file(url_coral_reef)

#set the connection the the database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')

#load the geodataframe created to PostGIS
gdf.to_postgis(
    con=engine,
    name= TABLE,
)




