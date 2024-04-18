def forma_correta(ideia):
    ideia = ideia.lower()
    if ideia == 'oposicao' or ideia == 'contrariedade':
        return 'mas'
    elif ideia == 'quantidade' or ideia == 'intensidade':
        return 'mais'
    else:
        return 'Entrada inválida'

ideia = input()
print(forma_correta(ideia))