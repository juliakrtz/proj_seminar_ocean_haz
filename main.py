from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from  shapely.geometry import Point as Shapely_pt, mapping
from geojson import Point as Geoj_pt, Polygon as Geoj_polygon, Feature, Featurecollection


#create Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

#use the application object as a parameter to create an object of class SQLAlchemy
db = SQLAlchemy(app)

#create the columns, matches table from postgis
class sharkattacks(db.Model):
    __tablename__ = "shark_attacks"
    __table_args__ = {"schema": "public"}
    id = db.Columb(db.Integer, primary_key = True)
    date_attack = db.Column(db.timestamp()), 
    time_attack = db.Column(db.timestamp()),
    island = db.Column(db.varchar()),
    location_attack = db.Column(db.varchar()),
    location_attack_2 = db.Column(db.varchar()),
    dist_from_shore = db.Column(db.varchar()),
    activity = db.Column(db.varchar()),
    water_clarity = db.Column(db.integer()),
    ocean_depth = db.Column(db.integer()), 
    shark_type = db.Column(db.varchar()),
); 

@app.route('/')
def index():
    return render_template('') #put html here 




if __name__ == '__main__':
    app.run(debug=TRUE) 

#to create a class
    # id = db.Column(db.Integer, primary_key=True)
    # pickup_datetime = db.Column(db.DateTime())
    # dropoff_datetime = db.Column(db.DateTime())
    # passenger_count = db.Column(db.Integer)
    # geojson = db.Column(db.Text)



    def __init__(self, date_attack, time_attack, island, location_attack, location_attack_2, dist_from_shore, activity, water_clarity, ocean_depth, shark_type):
        self.date_attack = date_attack