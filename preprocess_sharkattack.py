#import
import pandas as pd
import geopandas
import geocoder 
# import etl as e
import csv
import sqlalchemy as sql 
from sqlalchemy import create_engine 
from shapely.geometry import Point


DB_SCHEMA = "sa"
TABLE = "shark_attacks"

#path to shark attack csv file
shark_attacks = "data\original\shark_attacks.csv"

#path to shark attack csv file with coordinates
shark_attacks_geo = "data\processed\shark_attacks_geo.csv"

#convert csv file to dataframe
df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=";", header="infer")
df.insert(5, 'full_location', (df.Location + "," + df.Location_attack), allow_duplicates=False)


#geocoding function 
def geocoding(input_island):
    g = geocoder.osm(input_island, country_codes= 'us')
    return g.osm['x'], g.osm['y']

#geocode the location of shark attacks
def geocode(df: pd.DataFrame):
    ##apply function to dataframe in full_location column
        df['locations'] = df['Location'].apply(geocoding)
        df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
            index = df.index)
        return df

#convert the geocoded shark attacks to csv and save it
def write_csv(df, output_csv):
    df.to_csv(
        output_csv,
        sep= ";",
        quotechar = '"',        
        header=True,
        index=False,
        index_label=False,
        quoting=csv.QUOTE_NONNUMERIC, 
    )

#insert the data into the database
def insert_data(gdf: geopandas.GeoDataFrame, table: str, chunksize: int=100) -> None:
    """This function inserts the data into the database

    Args:
        df (pd.DataFrame): dataframe to be inserted
        schema (str): the name of the schema
        table (str): the name of the table
        chunksize (int): the number of rows to insert at the time
    """
    engine = sql.create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
        # with engine.connect() as con:
        #     tran = con.begin()
    gdf.to_postgis(
                name=table, #schema=schema,
                con=engine,
                chunksize=chunksize #, method="multi"
            )
    #         tran.commit()
    # except Exception as e:
    #     if 'tran' in locals():
    #         tran.rollback()
    #     (f"{e}")

# #run the geocoding to the dataframe
# df = geocode(df)

# #get the geocoded dataframe and store it as csv
# #this path was made in order to store the geocoded file and avoid running the geocoding everytime
# write_csv(df, shark_attacks_geo) 

#convert the geocoded shark attacks in csv to dataframe again
df_geocoded = pd.read_csv(shark_attacks_geo, sep=";", header="infer")

#convert dataframe to geodataframe
gdf = geopandas.GeoDataFrame(
    df_geocoded,
    crs= {'init': 'EPSG:4326'},
    geometry= geopandas.points_from_xy(df_geocoded.lon, df_geocoded.lat)
)
#print(gdf)

#insert the shark attacks to the database
#db = e.DBController(**config["database"])
insert_data(gdf=gdf, table=TABLE, chunksize=1000)


 
#df.head()

##upload geocoded dataframe to postgis

#set up database connection engine
# engine = create_engine('postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz')
# df.to_sql(
#     con=engine,
#     name= "shark_attacks"
# )
