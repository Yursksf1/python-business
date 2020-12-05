from flask import Flask
from markupsafe import escape
from flask import render_template

import random

app = Flask(__name__)


@app.route('/')
def play():
    lenguaje = 'C++'
    persona = 'Katterine'
    return render_template(
        'index.html', 
        lenguaje=lenguaje,
        persona=persona
    )


