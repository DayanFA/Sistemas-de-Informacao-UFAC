a,b,c = map(float, input().split())
if b+c >a and a+c > b and b+a > c:
    p= a+b+c
    print('Perimetro = {}' .format(p))
else:
    ar=((a+b)*c)/2
    print('Area = {}' .format(ar))