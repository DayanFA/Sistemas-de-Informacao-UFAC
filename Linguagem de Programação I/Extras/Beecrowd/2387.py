N = int(input())
consultas = []

for _ in range(N):
    consulta = tuple(map(int, input().split()))
    consultas.append(consulta)

consultas.sort(key=lambda x: x[1])

max_consultas = 1
ultimo_fim = consultas[0][1]

for i in range(1, N):
    inicio, fim = consultas[i]

    if inicio >= ultimo_fim:
        max_consultas += 1
        ultimo_fim = fim

print(max_consultas)
