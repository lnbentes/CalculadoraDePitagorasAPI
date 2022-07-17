from flask import Flask, request, jsonify
from src.server.Calculo import Calculo

app = Flask(__name__)
cal = Calculo()


@app.route("/")
def homePage():
    return "Bem vindo"


@app.route("/hipotenusa/<cateto_1>/<cateto_2>", methods=["GET"])
def hipotenusa(cateto_1, cateto_2):

    numero = {"hipotenusa": cal.hipotenusa(cateto_1, cateto_2)}
    return jsonify(numero)


@app.route("/cateto/<hipotenusa_entrada>/<cateto_entrada>", methods=["GET"])
def cateto(hipotenusa_entrada, cateto_entrada):

    numero = {"cateto": cal.cateto(hipotenusa_entrada, cateto_entrada)}
    return jsonify(numero)


if __name__ == '__main__':
    app.run()
