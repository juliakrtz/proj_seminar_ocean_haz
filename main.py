from imp import is_frozen_package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create Flask application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

db = SQLAlchemy(app)

class sharkattacks(db.Model):
    __tablename__ = "shark_attacks"
    #create the columns
    id = serial PRIMARY KEY, 
    date_attack timestamp, 
    time_attack timestamp,
    island varchar,
    location_attack varchar,
    location_attack_2 varchar,
    dist_from_shore varchar, 
    activity varchar,
    water_clarity integer, 
    ocean_depth integer,
    shark_type varchar
); 
    id = db.Column(db.Integer, primary_key=True)
    pickup_datetime = db.Column(db.DateTime())
    dropoff_datetime = db.Column(db.DateTime())
    passenger_count = db.Column(db.Integer)
    geojson = db.Column(db.Text)

