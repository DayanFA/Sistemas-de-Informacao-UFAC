n1=0
n2=0
n3=0
while True:
    x= int(input())
    if x== 1:
        n1 +=1
    if x== 2:
        n2 += 1
    if x == 3:
        n3 += 1
    if x == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}' .format(n1))
print('Gasolina: {}' .format(n2))
print('Diesel: {}' .format(n3))