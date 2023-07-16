ec=0
oc=0
pc=0
nc=0
for _ in range(5):
    v=int(input())
    if v%2==0:
        ec=ec+1
    else:
        oc= oc+1

    if v>0:
        pc= pc+1
    elif v<0:
        nc= nc+1
print('{} valor(es) par(es)'.format(ec))
print('{} valor(es) impar(es)'.format(oc))
print('{} valor(es) positivo(s)'.format(pc))
print('{} valor(es) negativo(s)'.format(nc))