""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])


@app.route('/')
def start_game(name=None):
	""" Return hello template at application root URL."""
	return render_template('menu.html', name=name)

@app.route('/madlibs')
def mad():
	return render_template('madlib.html')

@app.route('/catwalk')
def walkcat():
	return render_template('catwalk.html')