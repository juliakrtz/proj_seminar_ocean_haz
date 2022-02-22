#pre processing bottom type shapefile and loading it to db
import geopandas
import pandas 
from sqlalchemy import create_engine
import pyproj 

#pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  
#the code above was only used because of an issue with Julia's computer, may or may not need this when running on another computer 

#set the table name in the database
TABLE = "bottom_type"

#url where the geojson file is located
url_bottom_type = "https://opendata.arcgis.com/datasets/4780150a51064c37bc627e2dcc4df615_2.geojson"

#convert the geojson file to geodataframe
gdf = geopandas.read_file(url_bottom_type)

#set the connection the the database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')

#load the geodataframe created to PostGIS
gdf.to_postgis(
    con=engine,
    name=TABLE,
)
