from flask import Flask, render_template, jsonify, request, redirect #importing Flask and other modules
import sqlite3
import psycopg2 
import osgeo.ogr
import shapely
import shapely.wkt 
import geopandas as gpd 
import pandas as pd
import json 
#from  shapely.geometry import Point as Shapely_pt, mapping
#from geojson import Point as Geoj_pt, Polygon as Geoj_polygon, Feature, Featurecollection

#get bottom type geojson from inputted coordinates
def get_bottom_type(x,y,connection):
   #query that gives a Feature Collection object
   query_bottom_type = f'''SELECT jsonb_build_object(
      'type',     'FeatureCollection',
      'features', jsonb_agg(features.feature)
   )
   FROM (
   SELECT jsonb_build_object(
      'type',       'Feature',
      'id',         objectid,
      'geometry',   ST_AsGeoJSON(geometry)::jsonb,
      'properties', to_jsonb(inputs) - 'objectid' - 'geometry'
   ) AS feature
   FROM (SELECT 
      b.objectid, b.seabed, b.geometry
      FROM bottom_type as b
      WHERE st_intersects(b.geometry, 
                  st_transform(
                     st_buffer(
                        st_transform(
                           st_setsrid(
                              st_makepoint({x}, {y}),4326),26904),10000),4326)
                  )
   ) inputs) features'''

   #Reads the query and store it in a dataframe
   feature_collection_bottom_type = pd.read_sql(query_bottom_type, connection)

   #Getting geojson dictionary by calling iloc[0] on the jsonb_build_object column
   feature_collection_dict_bottom_type = feature_collection_bottom_type.iloc[0]['jsonb_build_object']

   #Converting to geojson
   bottom_feature_collection = json.dumps(feature_collection_dict_bottom_type)
   print(bottom_feature_collection)

   return  bottom_feature_collection

#get shark attacks geojson from inputted coordinates
def get_shark_attacks(x,y,connection):
   #query that gives a Feature Collection object
   query_shark_attacks = f'''SELECT jsonb_build_object(
      'type',     'FeatureCollection',
      'features', jsonb_agg(features.feature)
   )
   FROM (
   SELECT jsonb_build_object(
      'type',       'Feature',
      'id',          id,
      'geometry',   ST_AsGeoJSON(geometry)::jsonb,
      'properties', to_jsonb(inputs) - 'id' - 'geometry'
   ) AS feature
   FROM (SELECT 
      s."Date", s."Time", s."Location", s."Location_attack", s."Location_attack2", s.full_location, s."Location_attack3", s."Activity", s."Shark", s.geometry, s.id
      FROM shark_attacks as s
      WHERE st_intersects(s.geometry, 
                  st_transform(
                     st_buffer(
                        st_transform(
                           st_setsrid(
                              st_makepoint({x}, {y}),4326),26904),10000),4326)
                  )
   ) inputs) features'''

   #Reads the query and store it in a dataframe
   feature_collection_shark_attacks = pd.read_sql(query_shark_attacks, connection)

   #Getting geojson dictionary by calling iloc[0] on the jsonb_build_object column
   feature_collection_dict_shark_attacks = feature_collection_shark_attacks.iloc[0]['jsonb_build_object']

   #Converting to geojson
   shark_feature_collection = json.dumps(feature_collection_dict_shark_attacks)
   print(shark_feature_collection)

   return  shark_feature_collection

#get coral reefs geojson from inputted coordinates
def get_coral_reefs(x,y,connection):
   #query that gives a Feature Collection object
   query_coral_reefs = f'''SELECT jsonb_build_object(
      'type',     'FeatureCollection',
      'features', jsonb_agg(features.feature)
   )
   FROM (
   SELECT jsonb_build_object(
      'type',       'Feature',
      'id',         objectid,
      'geometry',   ST_AsGeoJSON(geometry)::jsonb,
      'properties', to_jsonb(inputs) - 'objectid' - 'geometry'
   ) AS feature
   FROM (SELECT 
      c.objectid, c.acres, c.geometry
      FROM coral_reefs as c
      WHERE st_intersects(c.geometry, 
                  st_transform(
                     st_buffer(
                        st_transform(
                           st_setsrid(
                              st_makepoint({x}, {y}),4326),26904),10000),4326)
                  )
   ) inputs) features'''

   #Reads the query and store it in a dataframe
   feature_collection_coral_reefs = pd.read_sql(query_coral_reefs, connection)

   #Getting geojson dictionary by calling iloc[0] on the jsonb_build_object column
   feature_collection_dict_coral_reefs = feature_collection_coral_reefs.iloc[0]['jsonb_build_object']

   #Converting to geojson
   coral_feature_collection = json.dumps(feature_collection_dict_coral_reefs)
   print(coral_feature_collection)

   return  coral_feature_collection

#get hazard areas geojson from inputted coordinates
def get_hazard_areas(x,y,connection):
   #query that gives a Feature Collection object
   query_hazard_areas = f'''SELECT jsonb_build_object(
      'type',     'FeatureCollection',
      'features', jsonb_agg(features.feature)
   )
   FROM (
   SELECT jsonb_build_object(
      'type',       'Feature',
      'id',         "Id",
      'geometry',   ST_AsGeoJSON(geometry)::jsonb,
      'properties', to_jsonb(inputs) - 'Id' - 'geometry'
   ) AS feature
   FROM (SELECT 
      h."Id", h.gridcode, h.geometry
      FROM hazard_areas as h
      WHERE st_intersects(h.geometry, 
                  st_transform(
                     st_buffer(
                        st_transform(
                           st_setsrid(
                              st_makepoint({x}, {y}),4326),26904),10000),4326)
                  )
   ) inputs) features'''

   #Reads the query and store it in a dataframe
   feature_collection_hazard_areas = pd.read_sql(query_hazard_areas, connection)

   #Getting geojson dictionary by calling iloc[0] on the jsonb_build_object column
   feature_collection_dict_hazard_areas = feature_collection_hazard_areas.iloc[0]['jsonb_build_object']

   #Converting to geojson
   hazard_feature_collection = json.dumps(feature_collection_dict_hazard_areas)
   print(hazard_feature_collection)

   return  hazard_feature_collection

#get connection to the Postgres database
def get_db_connection():
   connection = psycopg2.connect(database="geotech_ocean_haz", user="postgres", password = "postgres")
   return connection


#create Flask application
app = Flask(__name__)

# popup example 
# var geojson = L.geoJson(data, {
#       onEachFeature: function (feature, layer) {
#         layer.bindPopup(feature.properties.name + '<p><b> Line: ' + feature.properties.line + '</b></p>');
#         //EDIT HERE
#       }
#     });


#another popup example, leaftlet + python 
# markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
#                 {idd}.addTo(map).bindPopup('{brand}<br>{website}');".format(idd=idd, latitude=node.lat,\
#                                                                              longitude=node.lon,
#                                                                              brand=shop_brand,\
#                                                                              website=shop_website)

#another popup example, leaflet documenation page 
# L.marker([51.5, -0.09]).addTo(map)
#     .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
#     .openPopup();


#display popups for each variable point
bottom_type = "var {seabed} = L.seabed([{x}, {y}]);\ {seabed}.addTo(map).bindPopup" 
shark_attacks = "var {full_location} = L.full_location([{x}, {y}]);\ {full_location}.addTo(map).bindPopup" 
coral_reefs = "var {acres} = L.acres([{x}, {y}]);\ {acres}.addTo(map).bindPopup" 
hazard_areas = "var {gridcode} = L.gridcode([{x}, {y}]);\ {gridcode}.addTo(map).bindPopup" 


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"]) #importing flask and creating a home route which has both get and post methods
def gfg():
   if request.method == "POST": #if requesting method is post, we get the input data from HTML form
       # getting input with longitude (x) = lon from the HTML form
       x = request.form.get("lon")
       # getting input with latitude (y) = lat from the HTML form 
       y = request.form.get("lat")  
       print(x,y)

      #connecting to the database
       connection = get_db_connection()
       cursor = connection.cursor()
       
      # getting the separate data types to display on the map
       bottom_type = get_bottom_type(x,y,connection)
       shark_attacks = get_shark_attacks(x,y,connection)
       coral_reefs = get_coral_reefs(x, y, connection)
       hazard_areas = get_hazard_areas(x, y, connection)

       #render the result form with data
       return render_template("results.html", bottom_type = bottom_type, shark_attacks = shark_attacks, coral_reefs = coral_reefs, hazard_areas = hazard_areas)

   else:
      #render the input page
      return render_template("input.html")
   
if __name__=='__main__':
   app.run()