"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from FlaskWebProject import app

# import checkWeather

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
    print lon1
    print lat1

    print fromC
    print lon2
    print lat2
    print date
    # print request.args.list('from')
    # print request.args.list('lon1')
    # print request.args.list('lat1')
    # print request.args.list('to')
    # print request.args.list('lon2')
    # print request.args.list('lat2')
    # print request.args.list('date')
    return "info received"

# @app.route('/weather', methods=['GET'])
# def checkWeather():
    # currentWeather = checkWeather.currentConditions(long, lat, date)
