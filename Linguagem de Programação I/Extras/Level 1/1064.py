pc=0
ps=0
for _ in range(6):
    v=float(input())
    if v > 0:
        pc+= 1
        ps += v
av=ps/pc
print('{} valores positivos'.format(pc))
print('{:.1f}' .format(av))
