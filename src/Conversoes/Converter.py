class Converter:

    def converter_string_float(self, str_numero):
        numero_ponto = str_numero.replace(",", ".")
        return float(numero_ponto)
