N, M = map(int, input().split())

campo = []
for _ in range(N):
    linha = list(map(int, input().split()))
    campo.append(linha)

soma_maxima = 0

for linha in campo:
    soma = sum(linha)
    if soma > soma_maxima:
        soma_maxima = soma

for j in range(M):
    soma = 0
    for i in range(N):
        soma += campo[i][j]
    if soma > soma_maxima:
        soma_maxima = soma

print(soma_maxima)