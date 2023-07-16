N = int(input())
fila = list(map(int, input().split()))
M = int(input())
saiu = set(map(int, input().split()))

resultado = []
for pessoa in fila:
    if pessoa not in saiu:
        resultado.append(pessoa)

print(*resultado)