v=int(input())
print(v)
ns=[100, 50, 20, 10, 5, 2, 1]
for n in ns:
    q=v//n
    v = v%n
    print('{} nota(s) de R$ {:.2f}'.format(q,n).replace('.', ',')) 
