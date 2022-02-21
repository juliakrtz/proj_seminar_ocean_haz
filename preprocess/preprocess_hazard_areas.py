import geopandas
import pandas
from sqlalchemy import create_engine
import pyproj 

#pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  

#set the table name in the database
TABLE = "hazard_areas"

#path where is located the geojson file
url_hazard_areas = "data\original\hi_hazard_areas.shp"

#convert the geojson file to geodataframe
gdf = geopandas.read_file(url_hazard_areas)

#set the connection the the database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')

#load the geodataframe created to PostGIS
gdf.to_postgis(
    con=engine,
    name= TABLE,
)