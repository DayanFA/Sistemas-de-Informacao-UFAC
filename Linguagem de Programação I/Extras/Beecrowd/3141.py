nome = input()
da = input()
dn = input()
da, ma,aa = map(int, da.split('/'))
dn,mn,an = map(int, dn.split('/'))
if da == dn and ma == ma:
    print("Feliz aniversario!")
i = aa -an
if ma < mn or (ma == mn and da < dn):
    i -= 1
print(f'Voce tem {i} anos {nome}.')