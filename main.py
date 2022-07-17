import string

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calcular/<numero1>/<numero2>", methods=["GET"])
def calcular(numero1, numero2):
    numero = {"numero1": numero1,
              "numero2": numero2}
    return jsonify(numero)


app.run()
