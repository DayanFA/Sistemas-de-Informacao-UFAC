class Banco:
    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def calcular_impostos(self, manipulador):
        return manipulador.calcular_impostos(self._contas)