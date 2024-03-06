from math import sqrt, pi

class FormaGeometrica:
    def __init__(self):
        pass

    def inicializar(self):
        pass

    def mostrar_dados(self):
        pass

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio=None, diametro=None):
        super().__init__()
        if raio is not None:
            self.raio = raio
        elif diametro is not None:
            self.raio = diametro / 2
        else:
            self.raio = 0

    def inicializar(self):
        print("Inicializando circulo com raio:", self.raio)

    def mostrar_dados(self):
        print("Círculo de raio:", self.raio)

    def calcular_area(self):
        return pi * self.raio * self.raio

    def calcular_perimetro(self):
        return 2 * pi * self.raio

class Quadrilatero(FormaGeometrica):
    def __init__(self, lado1, lado2=None):
        super().__init__()
        if lado2 is not None:
            self.lado1 = lado1
            self.lado2 = lado2
        else:
            self.lado1 = self.lado2 = lado1

    def inicializar(self):
        print("Inicializando quadrilátero com lados:", self.lado1, self.lado2)

    def mostrar_dados(self):
        print("Quadrilátero de lados:", self.lado1, self.lado2)

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def inicializar(self):
        print("Inicializando triângulo com lados:", self.lado1, self.lado2, self.lado3)

    def mostrar_dados(self):
        print("Triângulo de lados:", self.lado1, self.lado2, self.lado3)

    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

circulo = Circulo(raio=5)
circulo.inicializar()
circulo.mostrar_dados()
print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

quadrilatero = Quadrilatero(lado1=4, lado2=6)
quadrilatero.inicializar()
quadrilatero.mostrar_dados()
print("Área:", quadrilatero.calcular_area())
print("Perímetro:", quadrilatero.calcular_perimetro())

triangulo = Triangulo(lado1=3, lado2=4, lado3=5)
triangulo.inicializar()
triangulo.mostrar_dados()
print("Área:", triangulo.calcular_area())
print("Perímetro:", triangulo.calcular_perimetro())
