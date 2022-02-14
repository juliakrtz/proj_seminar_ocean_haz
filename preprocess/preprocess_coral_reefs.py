#import
import geopandas
import pandas
from sqlalchemy import create_engine
import pyproj 

pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  

DB_SCHEMA = "sa"
TABLE = "coral_reefs"


url_coral_reef = "C:\Users\johnk\Desktop\proj_seminar\ocean_proj\proj_seminar_ocean_haz\hi_hazard_areas.shp"

gdf = geopandas.read_file(url_coral_reef)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
gdf.to_postgis(
    con=engine,
    name= TABLE,
)




