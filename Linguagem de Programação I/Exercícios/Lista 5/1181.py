x = int(input())
op = input()
matriz = []
for i in range(12):
    linha= []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
for j in range(12):
    soma += matriz[x][j]
media = soma/12
if op == 'S':
    print('{:.1f}'.format(soma))
if op == 'M':
    print('{:.1f}'.format(media))