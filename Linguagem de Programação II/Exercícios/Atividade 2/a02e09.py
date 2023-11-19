nomes = ['Ana', 'Carlos', 'Maria', 'João', 'Dayan']
comb = {(v, n2) for c, v in enumerate(nomes) for n2 in nomes[c + 1:]}
print(comb)
