#preprocess shark attacks data

import pandas as pd
import geocoder
from sqlalchemy import create_engine 

DB_SCHEMA = "sa"
TABLE = "shark_attacks"
DOWNLOAD_DIR = "data/original"
PROCESSED_DIR = "data/processed"

shark_attacks = "data\original\shark_attacks.csv"

df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=",", header="infer")

#geocode shark_attacks dataframe 
def geocoding(input_island):
    g = geocoder.osm(input_island)
    return g.osm['x'], g.osm['y']

df['locations'] = df['island'].apply(geocoding)
df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
        index = df.index)

df.head()


engine = create_engine("postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz")
gdf.to_postgis("shark_attacks", engine)