from flask import Flask, render_template

app = Flask(__name__)

@app.route('/catalogo')
def catalogo():
    productos = [
        {"nombre": "Teclado mecánico", "precio": 45.00, "stock": 5},
        {"nombre": "Monitor 24\"", "precio": 120.99, "stock": 2},
        {"nombre": "Webcam HD", "precio": 39.90, "stock": 0}
    ]

    return render_template("catalogo.html", catalogo=productos)


if __name__ == '__main__':
    app.run()