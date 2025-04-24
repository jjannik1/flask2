from flask import Flask, render_template

app = Flask(__name__)

class Pelicula:
    def __init__(self, nombre, año, protagonista):
        self.nombre = nombre
        self.año = año
        self.protagonista = protagonista

@app.route("/")
def hey():
    return "Hola"

@app.route("/estructura")
def estructura():
    peliculas = [
        "El lobo de Wall Street",
        "Harry Potter",
        "Volver al Futuro"
    ]

    lobo = {
        "Nombre": "El lobo de Wall Street",
        "Año": 2013,
        "Protagonista": "Leonardo DiCaprio"
    }

    volver = Pelicula("Volver al Futuro", 1985, "Michael J. Fox")

    return render_template("estructuras.html", peliculas=peliculas, destacado=lobo, favorita=volver)


if __name__ == "__main__":
    app.run()
