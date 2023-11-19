potencia = lambda x, y: x**y
base = [2, 3, 4]
expoente = [3, 2, 1]
resultado = map(potencia, base, expoente)
print(list(resultado))
