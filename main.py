from imp import is_frozen_package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create Flask application
app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Hello world"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=105)

#set URI to the database to use
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

#use the application object as a parameter to create an object of class SQLAlchemy
db = SQLAlchemy(app)

#declare shark_attack object model
class sharkattacks(db.Model):
    __tablename__ = "shark_attacks"
    #create the columns
    id = db.Column(db.Integer, primary_key= True) 
    date_attack = db.Column(db.DateTime()) 
    time_attack = db.Column(db.DateTime()) 
    island = db.Column(db.Integer)
    location_attack = db.Column(db.Integer)
    location_attack_2 = db.Column(db.Integer)
    dist_from_shore = db.Column(db.Integer)
    activity = db.Column(db.Integer)
    water_clarity = db.Column(db.Integer)
    ocean_depth = db.Column(db.Integer)
    shark_type = db.Column(db.Integer)



    def __init__(self, date_attack, time_attack, island, location_attack, location_attack_2, dist_from_shore, activity, water_clarity, ocean_depth, shark_type):
        self.date_attack = date_attack