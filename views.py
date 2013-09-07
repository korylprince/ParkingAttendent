from flask import render_template
from ParkingAttendent import app
from ParkingAttendent.models import *

@app.route("/")
def index():
    return render_template('index.html', lots=Lot.query.all())
