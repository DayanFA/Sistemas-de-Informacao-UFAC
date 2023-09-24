l = input()
n = input()
k=n.split()
d=0.0
kt=len(k)
for i in k:
    if l in i:
        d +=1
p= (d/kt)*100.0
print('{:.1f}'.format(p))