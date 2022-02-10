#pre processing bottom type shapefile and loading it to db
import geopandas
import pandas 
from sqlalchemy import create_engine
import pyproj 

pyproj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')  

#from pyproj import Transformer
#transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
#transformer.transform(12, 12)


DB_SCHEMA = "sa"
TABLE = "bottom_type"

url_bottom_type = "https://opendata.arcgis.com/datasets/4780150a51064c37bc627e2dcc4df615_2.geojson"

gdf = geopandas.read_file(url_bottom_type)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
gdf.to_postgis(
    con=engine,
    name=TABLE,
)
