from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def loop_for():
    equipos = [
        "REAL MADRID",
        "FC BARCELONA",
        "MILAN AC",
        "LIVERPOOL",
        "BAYERN MUNICH",
        "AJAX AMSTERD",
        "INTER MILAN",
        "JUVENTUS",
        "MANCHESTER UNITED",
        "OPORTO"
    ]

    equipos_cham = {
        "REAL MADRID": 14,
        "MILAN AC": 7,
        "LIVERPOOL": 6,
        "BAYERN MUNICH": 5,
        "AJAX AMSTERD": 4,
        "INTER MILAN": 3,
        "MANCHESTER UNITED": 3
    }

    return render_template("for_loop.html", teams=equipos, teams_dic=equipos_cham)


if __name__ =="__main__":
    app.run()
