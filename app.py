from flask import Flask
from markupsafe import escape
from flask import render_template

import random

app = Flask(__name__)


@app.route('/')
def play():
    return render_template('index.html')


