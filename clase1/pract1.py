from flask import Flask, render_template

app = Flask(__name__)

@app.route("/descuento")
def descuento():
    return render_template("")
