#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
With three Routes
"""
from flask import Flask
import re

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ First Route that display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb2():
    """ Second Route that display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Third Route that display C and text"""
    text = re.sub(r'_', ' ', text)
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
