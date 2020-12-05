from flask import Flask
from markupsafe import escape
import random

app = Flask(__name__)


@app.route('/juego/<int:numero>')
def play(numero):
    ran = random.randint(1, 10)
    print('ran', ran)
    if ran == numero: 
        return 'Adivinaste'
    else: 
        return 'sigue intentando'


