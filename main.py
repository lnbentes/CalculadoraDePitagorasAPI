from flask import Flask, jsonify
from src.Matematica.Calculo import Calculo
from src.Conversoes.Converter import Converter

app = Flask(__name__)
cal = Calculo()
conv = Converter()


@app.route("/")
def homePage():
    return "Bem vindo"


@app.route("/hipotenusa/<cateto_1>/<cateto_2>", methods=["GET"])
def hipotenusa(cateto_1, cateto_2):
    numero = {"resultado": cal.hipotenusa(cateto_1, cateto_2)}
    return jsonify(numero)


@app.route("/cateto/<hipotenusa_entrada>/<cateto_entrada>", methods=["GET"])
def cateto(hipotenusa_entrada, cateto_entrada):
    cateto_calculado = cal.cateto(hipotenusa_entrada, cateto_entrada)

    if cateto_calculado == "erro":
        return "Erro matemático: A hipotenusa tem que ser maior que o cateto", 400

    numero = {"resultado": cateto_calculado}
    return jsonify(numero)


if __name__ == '__main__':
    app.run()
