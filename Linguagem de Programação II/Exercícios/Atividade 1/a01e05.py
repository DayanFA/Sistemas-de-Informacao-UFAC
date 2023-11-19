# Leia uma frase digitada pelo usuário:

frase = input('Digite uma frase: ')

freq = {}

# Processamento da frase para obter a frequência das letras

for i in frase:

    #Ignore caracteres brancos e pontuação:

    if i.isalpha():
        i = i.lower()
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

# Calcule e mostre a frequência relativa de cada letra na frase,

total = sum(freq.values())
freqre = {}
for c, v in freq.items():
    freqre[c] = v / total

# Em ordem:

for l in sorted(freqre.keys()):
    print(f"A frequência relativa de '{l}' é {freqre[l]:.2%}.")
