def limpa(entrada):
    iterator = iter(entrada)
    l = next(iterator)
    if l:
        yield l
        for i in iterator:
            if i != l:
                yield i
                l = i
entrada = 'aaabbacabbbd'
saida = list(limpa(entrada))
print(saida)
