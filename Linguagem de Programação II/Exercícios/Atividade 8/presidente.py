from funcionario import Funcionario

class Presidente(Funcionario):
    def get_bonus(self):
        return self.salario * 0.5 + 1000