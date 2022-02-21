import pandas as pd
import json

# #get bottom type geojson from inputted coordinates
# def get_bottom_type(x,y,connection):
#    #query that gives a Feature Collection object
#    query_bottom_type = f'''SELECT jsonb_build_object(
#       'type',     'FeatureCollection',
#       'features', jsonb_agg(features.feature)
#    )
#    FROM (
#    SELECT jsonb_build_object(
#       'type',       'Feature',
#       'id',         objectid,
#       'geometry',   ST_AsGeoJSON(geometry)::jsonb,
#       'properties', to_jsonb(inputs) - 'objectid' - 'geometry'
#    ) AS feature
#    FROM (SELECT 
#       b.objectid, b.seabed, b.geometry
#       FROM bottom_type as b
#       WHERE st_intersects(b.geometry, 
#                   st_transform(
#                      st_buffer(
#                         st_transform(
#                            st_setsrid(
#                               st_makepoint({x}, {y}),4326),26904),10000),4326)
#                   )
#    ) inputs) features'''

#    #Reads the query and store it in a dataframe
#    feature_collection_bottom_type = pd.read_sql(query_bottom_type, connection)

#    #Getting geojson dictionary by calling iloc[0] on the jsonb_build_object column
#    feature_collection_dict_bottom_type = feature_collection_bottom_type.iloc[0]['jsonb_build_object']

#    #Converting to geojson
#    bottom_feature_collection = json.dumps(feature_collection_dict_bottom_type)
#    print(bottom_feature_collection)

#    return  bottom_feature_collection

