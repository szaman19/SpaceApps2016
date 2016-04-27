"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from FlaskWebProject import app

import HazardAlert
import checkWeather

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/apiTest')
def awesome():
    """Renders apiTest"""
    return render_template(
        'apiTest.html',
        title='AWESOME',
    )

@app.route('/trial', methods=['GET'])
def apiTrial():
    return jsonify({"Hello":"World"});


@app.route('/extremeHazard', methods = ['GET'])
def checkHazards():
    info =  request.args.items()
    # print type(request.args.items())
    to = info[0]
    lon1 = info[1]
    lat1 = info[2]
    lat2 = info[3]
    date = info[4]
    fromC = info[5]
    lon2 = info[6]

    print to
    lon1 = float(lon1[1])
    lat1 = float(lat1[1])

    print fromC
    lon2 = float(lon2[1])
    lat2 =  float(lat2[1])

    # print HazardAlert.findHazard(lon2, lat2)
    # print HazardAlert.findHazard(lon1, lat1)
    month =  date[1][0:2]
    day =  date[1][3:5]
    print lon1
    print lat1
    print month
    print day

    try:
        dicto = checkWeather.weather(lat1,lon1,int(month),int(day))
        print dicto
    except Exception as e:
        print e
    # return jsonify(dicto)
    return "info received"

@app.route('/weather', methods=['GET'])
def checkWeather():
    info =  request.args.items()
     # print type(request.args.items())
    to = info[0]
    lon1 = info[1]
    lat1 = info[2]
    lat2 = info[3]
    date = info[4]
    fromC = info[5]
    lon2 = info[6]

    print to
    lon1 = float(lon1[1])
    lat1 = float(lat1[1])

    print fromC
    lon2 = float(lon2[1])
    lat2 =  float(lat2[1])

     # print HazardAlert.findHazard(lon2, lat2)
     # print HazardAlert.findHazard(lon1, lat1)
    month =  date[1][0:2]
    day =  date[1][3:5]
    print lon1
    print lat1
    print month
    print day

    # try:
    #     dicto = checkWeather.weather(lat1,lon1,int(month),int(day))
    #     print dicto
    # except Exception as e:
    #     print e
    return "item received"
    # currentWeather = checkWeather.currentConditions(long, lat, date)
