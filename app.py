from flask import Flask, request, render_template
from markupsafe import escape

import random

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def play():
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 + valor_2

    return render_template(
        'index.html',
        respuesta=respuesta
    )


