class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_encerrada']

    _numero_conta = 0

    def __init__(self, cli, sal, lim):
        Conta._numero_conta += 1
        self._numero = Conta._numero_conta
        self._titular = cli
        self._saldo = sal
        self._limite = lim
        self._encerrada = 0  

    def depositar(self, valor):
        self._saldo += valor

    def encerrar_conta(self):
        if self._saldo == 0:
            self._encerrada = 1  
            print(f"Conta {self._numero} encerrada.")
        else:
            print("Não é possível encerrar a conta. O saldo deve ser zero.")

    def sacar(self, valor):
        if self._saldo - valor < -self._limite:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
    def extrato(self):
        print(f"Extrato da Conta {self._numero}:")
        print(f"Titular: {self._titular._nome}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        print(f"Limite: R$ {self._limite:.2f}")
        print()
