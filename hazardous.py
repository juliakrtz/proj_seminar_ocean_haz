import numpy as np
import fiona
import rasterio
import rasterio.features
from shapely.geometry import shape, mapping
from shapely.geometry.multipolygon import MultiPolygon

# Read input band with Rasterio
with rasterio.open('data/processed/output_3mile.tif') as src:
    crs = src.crs
    src_band = src.read(1)
    # Keep track of unique pixel values in the input band
    unique_values = np.unique(src_band)
    # Polygonize with Rasterio. `shapes()` returns an iterable
    # of (geom, value) as tuples
    shapes = list(rasterio.features.shapes(src_band, transform=src.transform))


shp_schema = {
    'geometry': 'MultiPolygon',
    'properties': {'pixelvalue': 'int'}
}

# Get a list of all polygons for a given pixel value
# and create a MultiPolygon geometry with shapely.
# Then write the record to an output shapefile with fiona.
# We make use of the `shape()` and `mapping()` functions from
# shapely to translate between the GeoJSON-like dict format
# and the shapely geometry type.
with fiona.open('output.shp', 'w', 'ESRI Shapefile', shp_schema, crs) as shp:
    for pixel_value in unique_values:
        polygons = [shape(geom) for geom, value in shapes
                    if value == pixel_value]
        multipolygon = MultiPolygon(polygons)
        shp.write({
            'geometry': mapping(multipolygon),
            'properties': {'pixelvalue': int(pixel_value)}
        })