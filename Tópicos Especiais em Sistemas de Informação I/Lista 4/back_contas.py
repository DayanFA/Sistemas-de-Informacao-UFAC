import datetime
from tkinter import messagebox


class Conta:
    _id_contador = 1

    def __init__(self, numero, cliente, saldo, banco):
        if saldo < 0:
            messagebox.showerror('Erro', 'Saldo inicial não pode ser negativo.')
            return
        self.__id = Conta._id_contador
        Conta._id_contador += 1
        self.__numero = numero
        self.__titular = cliente
        self.__banco = banco
        self.__saldo = saldo
        self.__operacoes = []

    def saque(self, valor):
        if valor < 0:
            messagebox.showerror('Erro', 'O valor do saque deve ser positivo.')
            return False
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__registrar_operacao('Saque', valor)
            messagebox.showinfo('Sucesso', f'Saque de R${valor} realizado com sucesso.')
            return True
        else:
            messagebox.showerror('Erro', 'Saldo insuficiente para o saque.')
            return False

    def deposito(self, valor):
        if valor < 0:
            messagebox.showerror('Erro', 'O valor do depósito deve ser positivo.')
        else:
            self.__saldo += valor
            self.__registrar_operacao('Depósito', valor)
            messagebox.showinfo('Sucesso', f'Depósito de R${valor} realizado com sucesso.')

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return str(self.__numero)

    def get_titular(self):
        return self.__titular

    def get_banco(self):
        return self.__banco

    def get_id(self):
        return self.__id

    def get_operacoes(self):
        return self.__operacoes

    def __registrar_operacao(self, tipo, valor):
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__operacoes.append((data, tipo, valor))


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo, taxa_juros, banco):
        super().__init__(numero, cliente, saldo, banco)
        if taxa_juros < 0:
            messagebox.showerror('Erro', 'A taxa de juros não pode ser negativa.')
            return
        self.__taxa_juros = taxa_juros

    def atualizar_saldo_com_juros(self):
        novo_saldo = self.get_saldo() * (1 + self.__taxa_juros)
        self.deposito(novo_saldo - self.get_saldo())
        messagebox.showinfo('Sucesso', f'Saldo atualizado com juros de {self.__taxa_juros * 100}%.')


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo, taxa_desconto, banco):
        super().__init__(numero, cliente, saldo, banco)
        if taxa_desconto < 0:
            messagebox.showerror('Erro', 'A taxa de desconto não pode ser negativa.')
            return
        self.__taxa_desconto = taxa_desconto

    def saque(self, valor):
        valor_com_taxa = valor + (valor * self.__taxa_desconto)
        if super().saque(valor_com_taxa):
            messagebox.showinfo('Sucesso',
                                f'Valor: R$ {valor:.2f}\nTaxa: R$ {valor * self.__taxa_desconto}.')
        else:
            messagebox.showerror('Erro', 'Saldo insuficiente.')

    def deposito(self, valor):
        valor_com_desconto = valor - (valor * self.__taxa_desconto)
        super().deposito(valor_com_desconto)
        messagebox.showinfo('Sucesso', f'Depósito realizado com desconto de R${valor * self.__taxa_desconto}.')
