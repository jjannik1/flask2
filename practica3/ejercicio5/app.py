from flask import Flask, render_template

app = Flask(__name__)

@app.route('/admin/usuarios')
def users():
    usuarios = [
        {"nombre": "Ana", "rol": "admin", "activo": True, "publicaciones": 12},
        {"nombre": "Luis", "rol": "usuario", "activo": False, "publicaciones": 3},
        {"nombre": "Carmen", "rol": "usuario", "activo": True, "publicaciones": 7},
        {"nombre": "Pedro", "rol": "admin", "activo": True, "publicaciones": 10}
    ]
    contactv = 0
    for usuario in usuarios:
        if usuario["activo"] == True:
            contactv = contactv + 1

    contro = 0
    for usuari in usuarios:
        if usuari["rol"]=="admin":
            contro = contro + 1


    return render_template("usuarios.html", usuarios=usuarios, contro=contro, contactv=contactv)

if __name__ == '__main__':
    app.run()