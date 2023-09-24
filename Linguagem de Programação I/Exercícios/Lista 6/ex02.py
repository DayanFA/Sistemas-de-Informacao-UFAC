class Porta:
    def __init__(self, cor, dimensaoX, dimensaoY, dimensaoZ):
        self.aberta = False
        self.cor = cor
        self.dimensaoX = dimensaoX
        self.dimensaoY = dimensaoY
        self.dimensaoZ = dimensaoZ

    def abre(self):
        self.aberta = True

    def fecha(self):
        self.aberta = False

    def pinta(self, cor):
        self.cor = cor

    def esta_aberta(self):
        return self.aberta


p = Porta("Marrom", 80, 200, 5)
p.abre()
p.fecha()
p.pinta("Azul")
p.pinta("Turquesa ")
print(f"A porta está aberta? {p.aberta}")
print(f"A cor da porta é {p.cor}")
print(f"As dimensões da porta é --> X: {p.dimensaoX}, Y: {p.dimensaoY}, Z: {p.dimensaoZ}")
