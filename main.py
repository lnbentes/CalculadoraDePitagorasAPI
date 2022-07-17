import string

from flask import Flask, request

app = Flask(__name__)


@app.route("/numero/<numero1>", methods=["GET"])
def calcular(numero1):
    numero = numero1
    return numero


@app.route("/numero")
def bola():
    return "usuario"


app.run()
