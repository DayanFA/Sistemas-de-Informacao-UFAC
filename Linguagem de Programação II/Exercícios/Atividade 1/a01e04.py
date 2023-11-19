# Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor:

tempos = {}

# Uma pista de corrida permite 10 voltas para cada um de 6 corredores:

for i in range(1, 7):
    nomec = input(f"Digite o nome do {i} corredor: ")
    tempoc = []
    for v in range(1, 11):
        t = float(input(f"Digite o tempo em segundos para a volta {v} do corredor {nomec}: "))
        tempoc.append(t)
    tempos[nomec] = tempoc

# Diga de quem foi a melhor volta da prova e em que volta.

melhov = min(min(tempos.values()))
for c, v in tempos.items():
    if melhov in v:
        melhorvol = v.index(melhov) + 1
        corredormel = c
        break

# Calculando a média de tempos para cada corredor.

medias = {}
for c, v in tempos.items():
    medias[c] = sum(v) / len(v)

# Classificação final em ordem. O campeão é o que tem a menor média de tempos.

result = sorted(medias, key=medias.get)
print(f'A melhor volta da prova foi do corredor {corredormel} na volta {melhorvol}.')
for c, v in enumerate(result, 1):
    print(f'{c}º lugar: {v}')
