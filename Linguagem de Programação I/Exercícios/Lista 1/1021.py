v=float(input() + 0.001)
ns= [100, 50, 20, 10, 5, 2]
cs= [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for n in ns:
    qn=int(v//n)
    v = v%n
    print('{} nota(s) de R$ {:.2f}'.format(qn, n))

print('MOEDAS:')
v= v+0.001
for c in cs:
    qc=int(v//c)
    v = v % c
    print('{} moeda(s) de R$ {:.2f}'.format(qc, c))