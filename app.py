"""
Introduction to flask, routing, render templates, and database use

author/github: Travis Anderson / tander29
"""
__author__ = "Travis Anderson"

from flask import Flask
from flask import render_template
from tinydb import TinyDB
import random
app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def index():
    """how change routing after choice made? """
    rdm_item = random.choice(db.all())
    return render_template('index.html', item=rdm_item)


@app.route('/all')
def all(data=None):
    return render_template('all.html', data=db.all())


if __name__ == "__main__":
    app.run(debug=True)
