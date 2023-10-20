#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
With two Routes
"""
from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb2():
    return 'HBNB!'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
