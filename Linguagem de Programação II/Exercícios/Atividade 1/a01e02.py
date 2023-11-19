# Que leia 5 números inteiros e os armazene em uma lista.

numeros = []
for i in range(5):
    n = int(input(f'Digite o {i+1} número do vetor:'))
    numeros.append(n)

# Armazene em uma lista de tal forma que:
# Todos os números maiores ou iguais que o primeiro fiquem ao lado direito.

primeiron = numeros[0]
direita = []
for x in numeros:
    if x >= primeiron:
        direita.append(x)

# Todos os menores fiquem ao lado esquerdo.

esquerda = []
for x in numeros:
    if x < primeiron:
        esquerda.append(x)

# Lista Organizada:

listaorg = esquerda + direita
print('Resultado:', listaorg)
