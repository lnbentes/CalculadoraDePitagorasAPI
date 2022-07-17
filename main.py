from flask import Flask, jsonify, render_template
from src.Matematica.Calculo import Calculo
from src.Conversoes.Converter import Converter

app = Flask(__name__)
cal = Calculo()
conv = Converter()


@app.route("/")
def home_page():
    return render_template("Home_page.html")


@app.route("/hipotenusa/<cateto_1>/<cateto_2>", methods=["GET"])
def hipotenusa(cateto_1, cateto_2):
    """
        1- Realiza os cálculos matemáticos estrutura em um dicionário.
        2- Retorna o dicionário convertido para json.
    """
    numero = {"resultado": cal.hipotenusa(cateto_1, cateto_2)}
    return jsonify(numero)


@app.route("/cateto/<hipotenusa_entrada>/<cateto_entrada>", methods=["GET"])
def cateto(hipotenusa_entrada, cateto_entrada):
    cateto_calculado = cal.cateto(hipotenusa_entrada, cateto_entrada)

    # Retorna status 400 se o cateto for maior que a hipotenusa
    if cateto_calculado == "erro":
        return "Erro matemático: A hipotenusa tem que ser maior que o cateto", 400
    numero = {"resultado": cateto_calculado}
    return jsonify(numero)


if __name__ == '__main__':
    app.run()
