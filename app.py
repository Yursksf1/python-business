from flask import Flask
from markupsafe import escape
import random

app = Flask(__name__)


@app.route('/')
def play():
    return 'hola mundo'


