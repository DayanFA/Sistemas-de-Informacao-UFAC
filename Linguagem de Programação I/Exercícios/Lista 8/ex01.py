palavras = ['inefável', 'grill', 'faz', 'batata', 'ruim', '.', 'A', 'exceção', 'é', 'quando', 'faz', 'um', 'salgado', 'saboroso']
palavra = []

for x in palavras:
    try:
        letra = x[3]
        palavra.append(letra)
    except IndexError:
        pass

print(''.join(palavra))

