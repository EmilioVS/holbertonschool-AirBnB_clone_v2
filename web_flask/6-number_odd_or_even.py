#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, abort
from sys import argv
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def display_num(n):
    if n.isdigit():
        n = int(n)
        return f"{n} is a number"
    if not n.isdigit():
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    if n.isdigit():
        n = int(n)
        return render_template('5-number.html', title='HBNB', n=n)
    if not n.isdigit():
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
    if n.isdigit():
        if int(n) % 2 == 0:
            return render_template('6-number_odd_or_even.html', title='HBNB',
                                   n=n, o_or_e='even')
        else:
            return render_template('6-number_odd_or_even.html', title='HBNB',
                                   n=n, o_or_e='odd')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)