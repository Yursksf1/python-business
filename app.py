from flask import Flask, request, render_template
from markupsafe import escape

import random

app = Flask(__name__)


@app.route('/suma', methods=['POST', 'GET'])
def suma():
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 + valor_2

    return render_template(
        'index.html',
        respuesta=respuesta
    )


@app.route('/resta', methods=['POST', 'GET'])
def resta():
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 - valor_2

    return render_template(
        'index.html',
        respuesta=respuesta
    )



@app.route('/multiplicacion', methods=['POST', 'GET'])
def multiplicacion():
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 * valor_2

    return render_template(
        'index.html',
        respuesta=respuesta
    )


@app.route('/division', methods=['POST', 'GET'])
def division():
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 / valor_2

    return render_template(
        'index.html',
        respuesta=respuesta
    )


