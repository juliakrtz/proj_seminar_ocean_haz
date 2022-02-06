#preprocess bathymetry data
#1. extract mask from coastline.geojson 
#2. load it into the database

from osgeo import gdal, ogr

path_raster = r"data\original\bathymetry_hawaii.tif"

#open raster as a gdal dataset (confirm it, not sure)
input_raster = gdal.Open(path_raster)