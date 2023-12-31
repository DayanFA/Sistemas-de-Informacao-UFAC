class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._listaContas = []

    def atualizar_contas(self, taxa):
        saldo_total = 0
        for conta in self._listaContas:
            saldo_anterior = conta._saldo
            saldo_novo = conta.atualiza(taxa)
            saldo_total += saldo_novo - saldo_anterior
            print(f'Saldo anterior: {saldo_anterior}, Saldo novo: {saldo_novo}')
        print(f'Saldo total de todas as atualizações: {saldo_total}')
