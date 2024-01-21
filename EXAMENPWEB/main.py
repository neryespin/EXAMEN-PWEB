# EXAMEN FINAL PROGRAMACIÓN WEB NERY ESPINOZA.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ''
    total_sin_descuento = 0
    total_con_descuento = 0
    descuento_aplicado = 0

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        tarros = int(request.form.get('tarros'))

        # Calcular el total sin des
        total_sin_descuento = tarros * 9000

        # Calcular desc según la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        # Calcular el des en pesos
        descuento_en_pesos = total_sin_descuento * descuento

        # Aplicar des al total
        total_con_descuento = total_sin_descuento - descuento_en_pesos

        descuento_aplicado = descuento_en_pesos

    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                           total_con_descuento=total_con_descuento, descuento_aplicado=descuento_aplicado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido Administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido Usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True, port=5001)