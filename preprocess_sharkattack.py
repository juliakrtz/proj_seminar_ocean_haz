#import
import pandas as pd
import geopandas
import geocoder 
import etl as e
import csv
import sqlalchemy as sql 
from sqlalchemy import create_engine 


DB_SCHEMA = "sa"
TABLE = "shark_attacks"

#path to shark attack csv file
shark_attacks = "data\original\shark_attacks.csv"

#path to shark attack csv file with coordinates
shark_attacks_geo = "data\processed\shark_attacks_geo.csv"

#convert csv file to dataframe
df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=",", header="infer")

#geocoding function 
# def geocoding(input_island):
#     g = geocoder.osm(input_island)
#     return g.osm['x'], g.osm['y']

# #geocode the location of shark attacks
# def geocode(df: pd.DataFrame):
#     ##apply function to dataframe in island column 
#     df['locations'] = df['island'].apply(geocoding)
#     df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
#             index = df.index)
#     return df

#convert the dataframe with the coordinates to csv and save it
def write_csv(df):
    df.to_csv(
        shark_attacks_geo,
        sep= ";",
        quotechar = "'",        
        header=True,
        index=False,
        index_label=False,
        quoting=csv.QUOTE_NONNUMERIC, 
    )

def insert_data(df: pd.DataFrame, schema: str, table: str, chunksize: int=100) -> None:
    """This function abstracts the `INSERT` queries

    Args:
        df (pd.DataFrame): dataframe to be inserted
        schema (str): the name of the schema
        table (str): the name of the table
        chunksize (int): the number of rows to insert at the time
    """
    try: #where information is sent to the database 
        engine = sql.create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
        with engine.connect() as con:
            tran = con.begin()
            df.to_sql(
                name=table, schema=schema,
                con=con, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        (f"{e}")

#df = geocode(df)
#write_csv(df) 


#convert the shark attacks with coordinates to geodataframe
gdf = pd.read_csv(shark_attacks_geo, sep=";", header="infer")


#insert the shark attacks to the database
#db = e.DBController(**config["database"])
insert_data(df=gdf, schema = DB_SCHEMA, table=TABLE, chunksize=1000)


 
#df.head()

##upload geocoded dataframe to postgis

#set up database connection engine
# engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
# df.to_sql(
#     con=engine,
#     name= "shark_attacks"
# )
