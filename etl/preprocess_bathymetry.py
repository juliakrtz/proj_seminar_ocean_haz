#preprocess bathymetry data
#1. Clip raster from the 3 mile nautical boundary 
#2. Burn coastline boundary from raster 
#3. Load final raster into the database

from osgeo import gdal, ogr

path_raster = r"data\original\bathymetry_hawaii.tif"

#open raster as a gdal dataset (confirm it, not sure)
input_raster = gdal.Open(path_raster)