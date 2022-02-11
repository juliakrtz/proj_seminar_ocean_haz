from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create Flask application

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app 

from ocean_haz import create_app




# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

# db = SQLAlchemy(app)
