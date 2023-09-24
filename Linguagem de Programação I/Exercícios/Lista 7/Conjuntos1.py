l1 = input().split(',')
l2 = input().split(',')
for i in range(len(l1)):
    l1[i] = l1[i].strip().lower()
for i in range(len(l2)):
    l2[i] = l2[i].strip().lower()
c1 = set(l1)
c2 = set(l2)
pa = len(c1 & c2)
pd = len(l1) + len(l2) - len(c1 | c2)
pdd = len(c1 | c2)
pu = len(c1 ^ c2)
print('Pessoas nas duas listas ao mesmo tempo: {}'.format(pa))
print('Pessoas duplicadas: {}'.format(pd))
print('Total de pessoas distintas nas duas listas: {}'.format(pdd))
print('Pessoas apenas em uma das duas listas: {}'.format(pu))

