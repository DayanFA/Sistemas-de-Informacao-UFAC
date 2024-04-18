def vogal(letra):
    return letra in ['a', 'e', 'i', 'o', 'u']

risada = input()

soVogal = ''.join(list(filter(vogal, risada)))
invertido = soVogal[::-1]

print('S' if soVogal == invertido else 'N')