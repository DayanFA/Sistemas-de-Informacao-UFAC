def maisdois(n):
    return len(str(n)) > 2

n = [int(input(f'Digite o {i+1}º número: ')) for i in range(6)]
filtrado = list(filter(maisdois, n))
print(f'Números com mais de dois dígitos: {filtrado}')
