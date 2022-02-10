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

