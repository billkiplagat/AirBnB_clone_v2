#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
with Routes
"""
from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Fourth Route that display Python and text"""
    text = re.sub(r'_', ' ', text)
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_integer(n):
    """ Fifth Route that display C and text """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns a template at the /number_template/<n> route,
        expanding route"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns a template at the /number_odd_or_even/<n>
        route, display if the number is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
