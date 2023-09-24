from ex02 import Porta

class Casa:
    def __init__(self, cor):
        self.cor = cor
        self.porta1 = None
        self.porta2 = None
        self.porta3 = None

    def pinta(self, cor):
        self.cor = cor

    def quantas_portas_abertas(self):
        p = 0
        if self.porta1 and self.porta1.esta_aberta():
            p += 1
        if self.porta2 and self.porta2.esta_aberta():
            p += 1
        if self.porta3 and self.porta3.esta_aberta():
            p += 1
        return p

casa = Casa("amarelo")
casa.porta1 = Porta("Verde", 80, 200, 5)
casa.porta2 = Porta("Azul", 70, 190, 5)
casa.porta3 = Porta("Vermelho", 90, 210, 5)
casa.porta1.abre()
casa.porta2.abre()
casa.porta3.fecha()
print(f"CONSIDERE APENAS ABAIXO PARA ESSA CASA, ACIMA É A DO VIZINHO")
print(f"A cor da casa é {casa.cor}")
print(f"Número de portas abertas: {casa.quantas_portas_abertas()}")
