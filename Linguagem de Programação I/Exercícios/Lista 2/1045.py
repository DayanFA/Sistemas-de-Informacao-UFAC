a,b,c = map (float, input().split())
if b+c > a and a+c > b and b+c> c:
    if (a*a) == (b*b) + (c*c) or (b*b) == (a*a) + (c*c) or (c*c) == (b*b) + (a*a):
        print('TRIANGULO RETANGULO')
    elif (a*a) > (b*b) + (c*c) or (b*b) > (a*a) + (c*c)or (c*c)> (a*a) + (b*b):
        print('TRIANGULO OBTUSANGULO')
    elif (a*a) < (b*b) + (c*c)or (b*b) < (a*a) + (c*c) or (c*c)< (a*a) + (b*b): 
        print('TRIANGULO ACUTANGULO')
else: 
    print('NAO FORMA TRIANGULO')
if a==b==c:
    print('TRIANGULO EQUILATERO')
elif a==b or a==c or b==c:
    print('TRIANGULO ISOSCELES')