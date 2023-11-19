import time

inicio = time.time()
r1 = sum(1/n for n in range(1, 10**7))
fim = time.time()
print(f"Tempo da primeira: {fim - inicio}")

inicio = time.time()
r2 = sum([1/n for n in range(1, 10**7)])
fim = time.time()
print(f"Tempo da segunda: {fim - inicio}")

# A primeira expressão é preferível, além do tempo, pois ela
# evita a criação de uma lista grande na memória, o que pode
# consumir muita memória em casos de grande quantidade de elementos.
