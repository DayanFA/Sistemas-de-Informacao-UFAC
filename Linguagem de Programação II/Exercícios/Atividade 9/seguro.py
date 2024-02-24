from tributavel import TributavelMixin

class SeguroDeVida(TributavelMixin):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular

    def valor_imposto(self):
        return 34 + self._valor * 0.05