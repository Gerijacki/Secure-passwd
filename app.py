from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    longitud = int(request.form['longitud'])
    incluir_mayusculas = 'mayusculas' in request.form
    incluir_simbolos = 'simbolos' in request.form
    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_simbolos)
    return render_template('index.html', contrasena=contrasena)

if __name__ == "__main__":
    app.run(debug=True)
