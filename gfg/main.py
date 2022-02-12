from flask import Flask, render_template, jsonify, request, redirect #importing Flask and other modules
#from  shapely.geometry import Point as Shapely_pt, mapping
#from geojson import Point as Geoj_pt, Polygon as Geoj_polygon, Feature, Featurecollection


#create Flask application
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/geotech_ocean_haz'

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

