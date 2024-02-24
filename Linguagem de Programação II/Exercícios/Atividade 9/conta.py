import abc
from tributavel import TributavelMixin

class Conta(abc.ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal

class ContaCorrente(Conta, TributavelMixin):
    def valor_imposto(self):
        return self._saldo * 0.02

class ContaInvestimento(Conta, TributavelMixin):
    def valor_imposto(self):
        return self._saldo * 0.03