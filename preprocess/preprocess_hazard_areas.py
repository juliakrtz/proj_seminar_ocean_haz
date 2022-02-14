import geopandas
import pandas
from sqlalchemy import create_engine
import pyproj 

pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  

DB_SCHEMA = "sa"
TABLE = "hazard_areas"


url_hazard_areas = "hi_hazard_areas.shp"

gdf = geopandas.read_file(url_hazard_areas)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
gdf.to_postgis(
    con=engine,
    name= TABLE,
)