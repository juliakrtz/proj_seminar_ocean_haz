#import
import pandas as pd
import geopandas
import geocoder 
#from sqlalchemy import create_engine
import etl as e

#from preprocess.preprocess_coral_reefs import DB_SCHEMA

DB_SCHEMA = "sa"
TABLE = "shark_attacks"


shark_attacks = "data\original\shark_attacks.csv"
df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=",", header="infer")

#geocode shark_attacks dataframe 
def geocoding(input_island):
    g = geocoder.osm(input_island)
    return g.osm['x'], g.osm['y']

##apply function to dataframe in island column 
df['locations'] = df['island'].apply(geocoding)
df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
        index = df.index)

db = e.DBController(**config["database"])
db.insert_data(df, DB_SCHEMA, TABLE, chunksize=1000)

#df.head()

##upload geocoded dataframe to postgis

#set up database connection engine
# engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
# df.to_sql(
#     con=engine,
#     name= "shark_attacks"
# )
