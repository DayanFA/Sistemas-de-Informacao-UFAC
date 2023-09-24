t1 = tuple(input())
t2 = tuple(input())
u = ()
m = min(len(t1), len(t2))
for i in range(m):
    u += (t1[i], t2[i])
if len(t1) > m:
    u += t1[m:]
elif len(t2) > m:
    u += t2[m:]
print(u)
