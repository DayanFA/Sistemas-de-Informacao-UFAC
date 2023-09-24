n = int(input())
while n != 0:
    cont, dicio = 0, {}
    for i in range(n):
        nome = list(input().split())
        dicio[nome[0]] = nome[1]
    m = int(input())
    for i in range(m):
        nome, dife = list(input().split()), 0
        origi = dicio[nome[0]]
        for j in range(len(nome[1])):
            if origi[j] != nome[1][j]:
                dife += 1
                if dife > 1:
                    cont += 1
                    break
    print(cont)
    n = int(input())
