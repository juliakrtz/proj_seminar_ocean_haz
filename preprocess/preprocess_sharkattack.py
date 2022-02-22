import pandas as pd
import geopandas
import geocoder 
import csv
import sqlalchemy as sql 
from sqlalchemy import create_engine 
from shapely.geometry import Point
import pyproj

#proj.datadir.set_data_dir('C:\\Users\\johnk\\anaconda3\\envs\\ocean_haz\\Library\\share\\proj')

#set the table name in the database
TABLE = "shark_attacks"

#path to shark attack csv file
shark_attacks = "data\original\shark_attacks.csv"

#path to shark attack csv file with coordinates
shark_attacks_geo = "data\processed\shark_attacks_geo.csv"

#get the csv file and convert it to dataframe
df = pd.read_csv(shark_attacks, encoding = 'cp1252', sep=";", header="infer")
df.insert(5, 'full_location', (df.Location + "," + df.Location_attack), allow_duplicates=False)

#geocoding function 
def geocoding(input_island):
    """ Geocode location using Open Street Map data

        Args:
            input_island (string): the location we want to geocode

        Returns:
            x and y values for each location
    """
    g = geocoder.osm(input_island, country_codes= 'us')
    return g.osm['x'], g.osm['y']

#geocode the location of shark attacks
def geocode(df: pd.DataFrame):
        """ Geocode attribute "location" from dataframe and inserts the x and y values to the dataframe

            Args:
                df (dataframe): the dataframe which contains the "location" attribute we want to geocode

            Returns:
                dataframe with the (x,y) attributes
        """
        df['locations'] = df['Location'].apply(geocoding)
        df[['lon','lat']] = pd.DataFrame(df['locations'].tolist(), 
            index = df.index)
        return df

#convert the geocoded shark attacks to csv and save it
#this step is made in order to not repeat the geocoding function every time running file
def write_csv(df, output_csv):
    """ Convert dataframe to a csv file

        Args:
            df (dataframe): the dataframe we want to convert to csv
            output_csv (string): path to where we want to save the output csv

    """
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
    gdf.to_postgis(
                name=table, #schema=schema,
                con=engine,
                chunksize=chunksize #, method="multi"
            )

#Uncomment this if it is the 1s time running the file!
# #run the geocoding to the dataframe
# df = geocode(df)

#Uncomment this if it is the 1s time running the file!
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

#insert the shark attacks to the database
insert_data(gdf=gdf, table=TABLE, chunksize=1000)