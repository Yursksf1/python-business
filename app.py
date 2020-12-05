from flask import Flask, request, render_template
from markupsafe import escape

import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'indice.html'
    )

@app.route('/suma', methods=['POST', 'GET'])
def suma():
    titulo = 'suma'
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 + valor_2

    return render_template(
        'index.html',
        respuesta=respuesta,
        titulo=titulo,
    )


@app.route('/resta', methods=['POST', 'GET'])
def resta():
    titulo = 'resta'
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 - valor_2

    return render_template(
        'index.html',
        respuesta=respuesta,
        titulo=titulo
    )


@app.route('/multiplicacion', methods=['POST', 'GET'])
def multiplicacion():
    titulo = 'multiplicacion'
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 * valor_2

    return render_template(
        'index.html',
        respuesta=respuesta,
        titulo=titulo
    )


@app.route('/division', methods=['POST', 'GET'])
def division():
    titulo = 'division'
    respuesta = 'no tengo respuesta'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        valor_2 = int(request.form['valor_2'])

        respuesta = valor_1 / valor_2

    return render_template(
        'index.html',
        respuesta=respuesta,
        titulo=titulo
    )



@app.route('/juego', methods=['POST', 'GET'])
def juego():
    value_random = random.randint(1, 10)

    titulo = 'juego'
    respuesta = 'Vamos a jugar'
    if request.method == 'POST':
        valor_1 = int(request.form['valor_1'])
        if value_random == valor_1: 
            respuesta = 'Adivinaste!'
        else: 
            respuesta = 'Intenta otra vez! '


    return render_template(
        'content_juego.html',
        respuesta=respuesta,
        titulo=titulo,
    )
