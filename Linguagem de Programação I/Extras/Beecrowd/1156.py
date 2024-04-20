s = 0
denom = 1
for num in range(1, 40, 2):
    s += num / denom
    denom *= 2
print(f'{s:.2f}')