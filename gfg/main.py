from flask import Flask, render_template, jsonify, request, redirect #importing Flask and other modules
import sqlite3
import psycopg2 
import osgeo.ogr
import shapely
import shapely.wkt 
import geopandas as gpd 
#from  shapely.geometry import Point as Shapely_pt, mapping
#from geojson import Point as Geoj_pt, Polygon as Geoj_polygon, Feature, Featurecollection


#create Flask application
app = Flask(__name__)

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
       return redirect('/')
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()


def get_db_connection():
    conn = sqllite3.connect('geotech_ocean_haz.db')
    conn.row_factory = sqlite3.Row
    return conn 

@app.route('/')
def index():
    conn= get_db_connection()
    posts = conn.execute('SELECT * FROM coral_reefs').fetchall()
    conn.close() 
    return render_template('index.html', posts = posts)

connection = psycopg2.connect(database="geotech_ocean_haz", user="postgres", password = "postgres")
cursor = connection.cursor()

cursor.execute(f"""SELECT objectid, acres, featureuid, geometry 
                  FROM coral_reefs as c 
                  WHERE st_intersects(c.geometry, st_transform (st_buffer(st_transform(st_setsrid(st_makepoint({x},{y}),4326),26904),20000),4326))"""
)
connection.commit() 

rows_list=[]
for objectid,acres,featureuid, geometry in cursor:
    data= {'OBJECTID':objectid, 'ACRES':acres, 'FEATUREUID':featureuid, 'GEOMETRY':geometry}
    rows_list.append(data)
#gdf=gpd.GeoDataFrame(rows_list, crs='epsg:4326').set_index('OBJECTID')
#gdf.head()
print(rows_list)


# #create the columns, matches table from postgis
# class sharkattacks(db.Model):
#     __tablename__ = "shark_attacks"
#     __table_args__ = {"schema": "public"}
#     id = db.Columb(db.Integer, primary_key = True)
#     date = db.Column(db.timestamp()), 
#     time = db.Column(db.timestamp()),
#     location = db.Column(db.varchar()),
#     location_attack = db.Column(db.varchar()),
#     location_attack2 = db.Column(db.varchar()),
#     full_location = db.Column(db.varchar()),
#     location_attack3 = db.Column(db.varchar()),
#     activity = db.Column(db.varchar()),
#     water_clarity = db.Column(db.integer()),
#     water_depth = db.Column(db.integer()),
#     description =  db.Column(db.varchar()),
#     shark = db.Column(db.varchar())
#     lon = db.Column(db.Float()), 
#     lat = db.Column(db.Float())
# ); 

# @app.route('/')
# def index():
# 	return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=TRUE) 

