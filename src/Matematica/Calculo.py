import math

from src.Conversoes.Converter import Converter


class Calculo:
    conv = Converter()

    """
    1- Recebe os valores das variáveis em string e converte para float.
    2- Realiza a operação matematica.
    3- Formata para ter duas casas decimais depois do ponto e retorna como string.
    """
    def hipotenusa(self, cateto_1, cateto_2):
        cateto_numero_1 = self.conv.converter_string_float(cateto_1)
        cateto_numero_2 = self.conv.converter_string_float(cateto_2)

        hipotenusa_1 = math.sqrt((math.pow(cateto_numero_1, 2) + math.pow(cateto_numero_2, 2)))
        format_hipotenusa = "{:.2f}".format(hipotenusa_1)
        return format_hipotenusa

    """
        1- Recebe os valores das variáveis em string e converte para float.
        1.1- Se o cateto for maior que a hipotenusa returna uma mensagem de erro.
        2- Realiza a operação matematica.
        3- Formata para ter duas casas decimais depois do ponto e retorna como string.
    """
    def cateto(self, hipotenusa_entrada, cateto_entrada):
        hipotenusa_numero = self.conv.converter_string_float(hipotenusa_entrada)
        cateto_numero = self.conv.converter_string_float(cateto_entrada)

        if cateto_numero >= hipotenusa_numero:
            return "erro"
        cateto = math.sqrt((math.pow(hipotenusa_numero, 2) - math.pow(cateto_numero, 2)))
        format_cateto = "{:.2f}".format(cateto)
        return format_cateto
