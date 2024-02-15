from funcionario import Funcionario

class Secretaria(Funcionario):
    def get_bonus(self):
        pass

class SecretariaExecutiva(Secretaria):
    def get_bonus(self):
        return self.salario * 0.1 + 100

class SecretariaAdministrativa(Secretaria):
    def get_bonus(self):
        return 100