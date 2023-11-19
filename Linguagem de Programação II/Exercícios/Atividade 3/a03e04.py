def soma(entrada):
    for i in entrada:
        yield sum(i)

entrada = [(1, 2, 3), (5, 7), (99, 15, -5)]
saida = soma(entrada)
print(' '.join(map(str, saida)))