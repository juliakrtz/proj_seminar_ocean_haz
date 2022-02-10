#import
import geopandas
import pandas
from sqlalchemy import create_engine

DB_SCHEMA = "sa"
TABLE = "coral_reefs"


url_coral_reef = "https://opendata.arcgis.com/datasets/9229d814438349948c99b5e61a084418_7.geojson"

gdf = geopandas.read_file(url_coral_reef)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
gdf.to_postgis(
    con=engine,
    name= TABLE,
)




