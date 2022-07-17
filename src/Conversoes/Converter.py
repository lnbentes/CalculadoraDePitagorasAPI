class Converter:
    """
        1- Recebe os valores das variáveis em string e troca todas as vírgulas por pontos.
        2- Retorna o número convertido para float.
    """
    def converter_string_float(self, str_numero):
        numero_ponto = str_numero.replace(",", ".")
        return float(numero_ponto)
