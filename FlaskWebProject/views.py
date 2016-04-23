"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from FlaskWebProject import app

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
