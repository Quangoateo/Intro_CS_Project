from flask import Flask, Response, render_template 
from aimodel import testing_camera
import json
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/technologies')
def technologies ():
    return render_template("technologies.html")
@app.route('/Timeline')
def Timeline():
    return render_template("Timeline.html")

# load camera into html file .
@app.route('/camera')
def camera():
    return Response(testing_camera.generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')
# load data from data.json into html table, the data will be processed by javascript file script.js
@app.route('/loadData', methods =['GET'])
def loadData():
    data = json.load(open('static/database/data.json'))
    return data
#Sending data from database to frontend .
if __name__ == "__main__":
    app.run(debug=True)