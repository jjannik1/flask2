from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return "Hola Mundo"


@app.route("/hola")
def hola():
    return "Hola como estamos"


@app.route("/elegante")
def pagina():
    return """
    <html>
        <body>
            <p>Hola Mundo 2.0</p>
        </body>
    </html>
        """


@app.route("/primera")
def primera_template():
    return render_template("primera_pagina.html")

@app.route("/segunda")
def segunda_template():
    return render_template("segunda_pagina.html")

@app.route("/variables")
def variab():
    return render_template("variables.html", nombre="Jannik", curso="Python")


@app.route("/pedro")
def predro():
    return render_template("variables.html", nombre="Pedro", curso="Programacion")


"""Ejercicio 1: Calculadora de descuentos en productos
Contexto: Un pequeño e-commerce quiere mostrar el precio final de sus productos aplicando descuentos.
Objetivo del ejercicio: Crear un endpoint en Flask (/descuento) que reciba los siguientes datos en un diccionario kwargs:
nombre del producto.
precio original.
porcentaje de descuento.
La plantilla Jinja2 debe:
Mostrar el nombre del producto en mayúsculas.
Calcular el precio con descuento.
Mostrar una frase como: El producto Camiseta cuesta 25€, pero con el 20% de descuento te queda en 20€."""


@app.route('/descuento')
def descuento():
    kwarg = {
        "producto": "Camiseta",
        "precio_ori": 250,
        "descuento": 20
    }

    return render_template("descuento.html", **kwarg)



"""Ejercicio 2: Perfil de usuario con resumen de actividad
Contexto: En una red social, se quiere mostrar la información del perfil de un usuario con estadísticas.
Objetivo del ejercicio: Crear un endpoint en Flask (/perfil) que envíe a la plantilla Jinja2 un diccionario con:
nombre del usuario.
número de publicaciones.
número de seguidores y seguidos.
años registrados.
La plantilla debe:
Mostrar una frase como: "Hola, Marta. Llevas 3 años en la red. Has publicado 125 veces y sigues a 230 personas."
Calcular el ratio de publicaciones por año y mostrarlo.
Concatenar el nombre con algún mensaje personalizado.
"""


@app.route("/perfil")
def perfil():
    kwargs = {
        "user": "Juanjo",
        "publicaciones": 125,
        "seguidores": 230,
        "years": 4
    }
    return render_template("usuario.html", **kwargs)


"""Ejercicio 3: Resumen de carrito de compras
Contexto: En un sitio de compras online, al acceder al carrito se quiere mostrar el total de la compra.
Objetivo del ejercicio: Crear un endpoint Flask (/carrito) que envíe una lista de productos dentro de un kwargs:
productos = [
 {"nombre": "Teclado", "precio": 20.50, "cantidad": 2},
 {"nombre": "Ratón", "precio": 15.00, "cantidad": 1},
 {"nombre": "Monitor", "precio": 120.99, "cantidad": 1}
]

La plantilla debe:
Mostrar todos los productos y calcular el subtotal (precio * cantidad).
Mostrar el total de la compra sumando todos los subtotales.
Añadir un mensaje como: "¡Tienes 3 productos en tu carrito!"
Ampliación opcional: Calcular IVA y precio total con impuestos."""

@app.route("/carrito")
def carrito():
    productos = [
 {"nombre": "Teclado", "precio": 20.50, "cantidad": 2},
 {"nombre": "Ratón", "precio": 15.00, "cantidad": 1},
 {"nombre": "Monitor", "precio": 120.99, "cantidad": 1}
]
    linea = []
    total = 0
    longitud = 0
    for i in productos:
        subtotal = i["precio"] * i["cantidad"]
        linea.append((i["nombre"], subtotal))
        total += subtotal
        longitud += 1

    return render_template("carrito.html", linea=linea, total=total, longitud=longitud)


if __name__ == "__main__":
    app.run()
