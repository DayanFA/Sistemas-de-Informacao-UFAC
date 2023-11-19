# Faça um programa que leia duas strings do teclado:

s1 = input('Digite a primeira string: ')
s2 = input('Digite a segunda string: ')

# Conjuntos dos caracteres das strings:

set1 = set(s1)
set2 = set(s2)

# Caracteres do primeiro texto que não estão no segundo:

chrsnnseg = set1 - set2

print(f'Caracteres do primeiro texto que não estão no segundo: {chrsnnseg}')

# Caracteres do segundo texto que não estão no primeiro:

chrsnnpri = set2 - set1

print(f'Caracteres do segundo texto que não estão no primeiro: {chrsnnpri}')

# Caracteres que estão em ambos os textos:

chrscmm = set1 & set2

print(f'Caracteres que estão em ambos os textos: {chrscmm}')

# Número total de caracteres distintos em ambos os textos:

chrsncm = len(set1 | set2)

print(f'Número total de caracteres distintos em ambos os textos: {chrsncm}')
