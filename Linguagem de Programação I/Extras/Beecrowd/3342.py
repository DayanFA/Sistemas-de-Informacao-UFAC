n = int(input())
m = []
for i in range(n):
    v =[]
    for j in range(n):
        if (i+j) % 2 == 0:
            v.append('a')
        else:
            v.append('b')
    m.append(v)
b=0
p=0
for k in m:
    for k2 in k:
        if k2 == 'a':
            b +=1
        else:
            p +=1
print(f'{b} casas brancas e {p} casas pretas')