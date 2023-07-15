valores = input().split()
x= float (valores[0])
y= float (valores[1])
op= input()
erro=False
if op == '+':
    resultado= x+y
elif op=='-':
    resultado= x-y
elif op=='*':
    resultado= x*y
elif op=='/':
    resultado= x/y
elif op=='**':
    resultado= x**y
else:
    print('O operador solicitado não é suportado.')
erro=True
if erro!= True:
# if resultado == 0:
    print(x,op,y,'=', resultado)


