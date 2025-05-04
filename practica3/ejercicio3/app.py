from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pedido')
def pedido():
    pedido = [
        {"nombre": "Ratón", "precio": 15.00, "cantidad": 2},
        {"nombre": "Teclado", "precio": 30.00, "cantidad": 1},
        {"nombre": "USB 64GB", "precio": 10.00, "cantidad": 3}
    ]

    total = 0
    for i in pedido:
        total += i["precio"] * i["cantidad"]
    return render_template("pedido.html", pedido=pedido, total=total)

if __name__ == '__main__':
    app.run()