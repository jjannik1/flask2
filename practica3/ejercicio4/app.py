from flask import Flask, render_template

app = Flask(__name__)

@app.route('/perfil')
def perfil():
    usuario = {
        "nombre": "Marta",
        "correo": "marta@mail.com",
        "publicaciones": [
            {"contenido": "¡Hola! Soy nueva aquí", "fecha": "2024-04-01"},
            {"contenido": "Hoy aprendí Flask", "fecha": "2024-04-03"},
            {"contenido": "Me gusta programar", "fecha": "2024-04-05"}
        ]
    }
    return render_template("perfil.html", perfil=usuario)

if __name__ == '__main__':
    app.run()