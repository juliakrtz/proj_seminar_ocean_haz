#import
import geopandas
import pandas
from sqlalchemy import create_engine
import pyproj 

#pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  
#the code above was only used because of an issue with Julia's computer, may or may not need this when running on another computer 

#set the table name in the database
TABLE = "coral_reefs"

#url where the geojson file is located 
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




