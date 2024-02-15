from gerente import Gerente

class Diretor(Gerente):
    def get_bonus(self):
        return self.salario * 0.4