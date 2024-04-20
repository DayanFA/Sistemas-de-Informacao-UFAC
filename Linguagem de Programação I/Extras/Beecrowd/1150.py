x = int(input())
z = int(input())
while z <= x:
    z = int(input())
soma = x
cont = 1
while soma <= z:
    soma += x + cont
    cont += 1
print(cont)