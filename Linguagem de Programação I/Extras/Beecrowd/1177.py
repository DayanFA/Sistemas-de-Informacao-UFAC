t = int(input())
v = [None]*1000
for i in range(1000):
    v[i] = i % t
for i in range(1000):
    print(f'N[{i}] = {v[i]}')