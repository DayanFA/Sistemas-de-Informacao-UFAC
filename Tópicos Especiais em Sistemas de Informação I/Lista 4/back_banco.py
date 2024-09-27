from tkinter import messagebox


class Banco:
    def __init__(self, numero, nome):
        self.__num = numero
        self.__nome = nome
        self.__contas = []

    def get_numero(self):
        return str(self.__num)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def adicionar_conta(self, conta):
        if not any(c.get_numero() == conta.get_numero() for c in self.__contas):
            self.__contas.append(conta)
        else:
            messagebox.showerror('Erro', f'Conta {conta.get_numero()} já existe no banco.')

    def get_contas(self):
        return self.__contas

    def excluir_conta(self, numero):
        for conta in self.__contas:
            if conta.get_numero() == numero:
                if conta.get_saldo() == 0:
                    self.__contas.remove(conta)
                    messagebox.showinfo('Sucesso', 'Conta encerrada com sucesso.')
                    return
                else:
                    messagebox.showerror('Erro', 'A conta não pode ser encerrada, pois há saldo!')
                    return
        messagebox.showerror('Erro', f'Conta {numero} não encontrada.')

    def cliente_vinculado(self, cliente_id):
        return any(conta.get_titular().get_id() == cliente_id for conta in self.__contas)
