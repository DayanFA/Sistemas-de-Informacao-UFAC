from tkinter import messagebox


class Cliente:
    _id_contador = 1

    def __init__(self, nome, endereco, cpf):
        if not nome or not endereco:
            messagebox.showerror('Erro', 'Nome e endereço não podem estar vazios.')
            raise ValueError
        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror('Erro', 'CPF inválido. Deve conter 11 dígitos numéricos.')
            raise ValueError

        self.__id = Cliente._id_contador
        Cliente._id_contador += 1
        self.__nome = nome
        self.__endereco = endereco
        self.__CPF = cpf

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cpf(self):
        return self.__CPF

    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        if nome:
            self.__nome = nome
        else:
            messagebox.showerror('Erro', 'O nome não pode estar vazio.')

    def set_endereco(self, endereco):
        if endereco:
            self.__endereco = endereco
        else:
            messagebox.showerror('Erro', 'O endereço não pode estar vazio.')
