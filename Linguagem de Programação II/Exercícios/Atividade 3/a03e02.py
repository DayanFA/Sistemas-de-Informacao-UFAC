def infinita():
    n = 0
    while True:
        yield n
        n += 1

resu = infinita()
n = int(input('Quantos números imprimir:'))
for i in range(n):
    print(next(resu))