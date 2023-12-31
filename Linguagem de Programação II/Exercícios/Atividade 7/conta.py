class Conta:
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return f'Titular: {self._titular}, Saldo: {self._saldo}'
class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor - 0.10
        return self._saldo

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
    
class ContaEspecial(ContaCorrente):
    def __init__(self, n, cli, sal, limite):
        super().__init__(n, cli, sal)
        self._limite = limite

    def sacar(self, valor):
        if self._saldo + self._limite >= valor:
            self._saldo -= valor
        return self._saldo