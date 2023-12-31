class Emprestimo:
    __slots__ = ['_valor', '_parcelas', '_juros', '_conta', '_parcela_atual']

    taxa_juro_mensal = 0.02
    quantidade_emprestimos = 0
    _total_emprestimos = 0 


    def __init__(self, valor, parcelas, juros, conta):
        self._valor = valor
        self._parcelas = parcelas
        self._juros = juros
        self._conta = conta
        self._parcela_atual = 1
        Emprestimo._total_emprestimos += 1

        
    @classmethod
    def total_emprestimos(cls):
        return cls._total_emprestimos
    def calcular_valor_total(self):
        return self._valor * (1 + self._juros) ** self._parcelas

    def calcular_valor_parcela(self):
        return self.calcular_valor_total() / self._parcelas

    def parcelas_restantes(self):        
        return self._parcelas - self._parcela_atual
    
    def pagar_parcela(self):
        if self._parcela_atual <= self._parcelas:
            print(f"Pago {self._parcela_atual}/{self._parcelas} - Valor: {self.calcular_valor_parcela():.2f}")
            self._parcela_atual += 1
        else:
            print("Empréstimo já foi totalmente pago.")
