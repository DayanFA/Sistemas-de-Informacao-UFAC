from funcionario import Funcionario

class Gerente(Funcionario):
    def get_bonus(self):
        return self.salario * 0.3