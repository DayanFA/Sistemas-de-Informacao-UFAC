a, b, c = map(float, input().split())
pi= 3.14159
ta= (a*c)/2
ca=pi*c**2
tpa=((a+b)*c)/2
sa=b**2
ra=a*b
print('TRIANGULO: {:.3f}'.format(ta))
print('CIRCULO: {:.3f}'.format(ca))
print('TRAPEZIO: {:.3f}'.format(tpa))
print('QUADRADO: {:.3f}'.format(sa))
print('RETANGULO: {:.3f}'.format(ra))