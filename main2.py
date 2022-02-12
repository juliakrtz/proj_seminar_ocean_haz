from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn= get_db_connection()
    posts = conn.execute('SELECT * FROM coral_reefs').fetchall()
    conn.close() 
    return render_template('index.html', posts = posts)

def get_db_connection():
    conn = sqllite3.connect('geotech_ocean_haz.db')
    conn.row_factory = sqlite3.Row
    return conn 
