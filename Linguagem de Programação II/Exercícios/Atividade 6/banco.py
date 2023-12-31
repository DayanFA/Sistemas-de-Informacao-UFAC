class Banco:
    __slots__ = ['_num', '_nome', '_contas']

    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._contas = []

    def listar_contas(self):
        for conta in self._contas:
            conta.extrato()

    def incluir_conta(self, conta):
        self._contas.append(conta)
        print(f"Conta {conta._numero} incluída no banco.")

    def remover_conta(self, conta):
        if conta in self._contas:
            self._contas.remove(conta)
            print(f"Conta {conta._numero} removida do banco.")
        else:
            print("Conta não encontrada no banco.")
