from flask import Flask, render_template

app = Flask(__name__)

@app.route('/producto')
def producto():
    producto = {
        "nombre": "ratón inalámbrico",
        "descripcion": "Dispositivo ergonómico con conexión Bluetooth",
        "precio": 19.99
    }
    return render_template("producto.html", producto=producto)

if __name__ == '__main__':
    app.run()