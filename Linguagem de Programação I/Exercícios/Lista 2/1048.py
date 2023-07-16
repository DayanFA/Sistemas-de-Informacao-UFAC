a = float (input())
if 0.00 <= a <= 400.00:
    rg= a*0.15
    ns= rg+a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 15 %')
elif 400.01 <= a <= 800.00:
    rg= a*0.12
    ns= rg+a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 12 %')
elif 800.01 <= a <= 1200.00:
    rg= a*0.10
    ns= rg+a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 10 %')
elif 1200.01 <= a <= 2000.00:
    rg= a*0.07
    ns= rg+a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 7 %')
elif a > 2000.00:
    rg= a*0.04
    ns= rg+a
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 4 %')