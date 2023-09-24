class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def faz_aniversario(self):
        self.idade += 1


p = Pessoa("Dayan", 23)
p.faz_aniversario()
p.faz_aniversario()
print(f"Nome: {p.nome}, Idade: {p.idade}")
