v, n = map(int, input().split())
k = v * n
p=0
c=0
h=[]
for i in range(1, 10):
    p= i /10
    c= p * k
    c= str(c)
    c1,c2 = map(int,c.split('.'))
    if c2>0:
        c1 +=1
    h.append(c1)
print(*h)

