from flask import Flask, render_template
from datetime import  date

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    nombre_admin = "Francisco"
    tienda = "TecnoMarket"
    fecha = date.today()

    productos = [
        {"nombre": "",
         "precio": 0.0,
         "stock": 0,
         "categoria": ""}
    ]
    clientes = []



    return render_template("dashboard.html", nombre_admin=nombre_admin, tienda=tienda, fecha=fecha)

if __name__ == '__main__':
    app.run()