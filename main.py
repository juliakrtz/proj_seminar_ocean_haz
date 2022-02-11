from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from  shapely.geometry import Point as Shapely_pt, mapping
from geojson import Point as Geoj_pt, Polygon as Geoj_polygon, Feature, Featurecollection


#create Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

db = SQLAlchemy(app)

#create the columns, matches table from postgis
class sharkattacks(db.Model):
    __tablename__ = "shark_attacks"
    __table_args__ = {"schema": "public"}
    id = db.Columb(db.Integer, primary_key = True)
    date = db.Column(db.timestamp()), 
    time = db.Column(db.timestamp()),
    location = db.Column(db.varchar()),
    location_attack = db.Column(db.varchar()),
    location_attack2 = db.Column(db.varchar()),
    full_location = db.Column(db.varchar()),
    location_attack3 = db.Column(db.varchar()),
    activity = db.Column(db.varchar()),
    water_clarity = db.Column(db.integer()),
    water_depth = db.Column(db.integer()),
    description =  db.Column(db.varchar()),
    shark = db.Column(db.varchar())
    lon = db.Column(db.Float()), 
    lat = db.Column(db.Float())
); 

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=TRUE) 

#to create a class
    # id = db.Column(db.Integer, primary_key=True)
    # pickup_datetime = db.Column(db.DateTime())
    # dropoff_datetime = db.Column(db.DateTime())
    # passenger_count = db.Column(db.Integer)
    # geojson = db.Column(db.Text)

