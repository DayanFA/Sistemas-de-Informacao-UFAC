from functools import reduce
palavras = ["Isso", "vai", "ser", "rapido"]
resultado = reduce(lambda x, y: x + ' ' + y, palavras)
print(resultado)
