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
    """Renders awesome"""
    return render_template(
        'apiTest.html',
        title='AWESOME',
    )

@app.route('/trial', methods=['GET'])
def apiTrial():
    return jsonify({"Hello":"World"});


@app.route('/extremeHazard', methods = ['GET'])
def checkHazards():
    print 'Hello'
    print 'Hello'
    print request.args
    return "info received"

# @app.route('/weather', methods=['GET'])
# def checkWeather():
    # currentWeather = checkWeather.currentConditions(long, lat, date)
