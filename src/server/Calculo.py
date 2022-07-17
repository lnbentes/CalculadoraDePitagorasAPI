import math


class Calculo:

    def hipotenusa(self, cateto_1, cateto_2):

        cateto_ponto_1 = cateto_1.replace(",", ".")
        cateto_ponto_2 = cateto_2.replace(",", ".")

        hipotenusa_1 = math.sqrt((math.pow(float(cateto_ponto_1), 2) + math.pow(float(cateto_ponto_2), 2)))
        format_hipotenusa = "{:.2f}".format(hipotenusa_1)
        return format_hipotenusa

    def cateto(self, hipotenusa_entrada, cateto_entrada):

        hipotenusa_ponto = hipotenusa_entrada.replace(",", ".")
        cateto_ponto = cateto_entrada.replace(",", ".")

        h_1 = float(hipotenusa_ponto)
        c_1 = float(cateto_ponto)

        if c_1 >= h_1:
            return "Math erro a hipotenusa tem que ser maior que o cateto"
        cateto = math.sqrt((math.pow(h_1, 2) - math.pow(c_1, 2)))
        format_cateto = "{:.2f}".format(cateto)
        return format_cateto

