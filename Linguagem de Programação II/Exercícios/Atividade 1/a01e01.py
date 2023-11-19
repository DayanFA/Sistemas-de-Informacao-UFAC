# Função para gerar números pseudoaleatórios, era muito mais facil só colocar import random:
#E não tem muito oq fazer, vai ser "aleatorio", mas mostrando os mesma quantidade sempre, então ta ai

def gerar_aleatorio(s):
    a = 1664525
    c = 1013904223
    m = 2**32
    while True:
        s = (a * s + c) % m
        #esse yield retorna em pausa, o proximo da sequencia.
        yield s % 6 + 1

# use uma lista de frequência

freq = [0, 0, 0, 0, 0, 0]
result = []

# Inicializar o gerador.

g = gerar_aleatorio(1)

# Lance o dado 100 vezes e armazene os resultados em uma lista.

for _ in range(100):
    n = next(g)
    result.append(n)
    freq[n - 1] += 1

# Resultado da simulação de um lançamento de dados, quantas vezes cada valor foi conseguido.

for c, v in enumerate(freq):
    print(f'O número {c + 1} apareceu {v} vezes.')
