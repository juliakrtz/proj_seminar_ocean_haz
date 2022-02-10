#preprocess bathymetry data
#1. Clip raster from the 3 mile nautical boundary 
#3. Load final raster into the database

#import standard modules
from click import password_option
from osgeo import gdal, ogr
import psycopg2
import os

#path to original bathymetry raster filer
path_raster = r"data\original\bathymetry_hawaii.tif"

#open raster as a gdal dataset (confirm it, not sure)
input_raster = gdal.Open(path_raster)

#path to 3 mile nautical boundary 
input_shape_3mile = "https://opendata.arcgis.com/datasets/82fb905c78064559905c8d932b63478b_31.geojson"

#path to store output raster file with 3 mile clipped
output_raster_3mile = "data\processed/output_3mile.tif"

# #path to coastline  of hawaii 
# input_shape_coastline = "https://opendata.arcgis.com/datasets/045b1d5147634e2380566668e04094c6_3.geojson"

# #path to final bathymetry raster
# output_raster_coastline = "data\processed/output_coastline.tif"

#clip raster with 3 mile nautical geojson
ds = gdal.Warp(output_raster_3mile,
              input_raster,
              cropToCutline=True,
              cutlineDSName = input_shape_3mile,
              format = 'GTiff',
              dstNodata = -9999) # select the no data value
ds=None #close the dataset


conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    dbname = 'geotech_ocean_haz',
    password = 'postgres'
    )
curs = conn.cursor()
curs.execute("SET postgis.gdal_enabled_drivers = 'ENABLE_ALL';")
os.system('raster2pgsql "%s" > temp.sql'%output_raster_3mile)
curs.execute(open('temp.sql','r').read())


