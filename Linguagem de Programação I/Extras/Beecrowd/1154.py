soma = cont = 0
idade = int(input())
while idade >= 0:
    soma += idade
    cont += 1
    idade = int(input())
media = soma / cont
print(f'{media:.2f}')