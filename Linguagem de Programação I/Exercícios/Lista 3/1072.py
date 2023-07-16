N = int(input())
count_in = 0
count_out = 0
for _ in range(N):
    X = int(input()) 
    if 10 <= X <= 20:
        count_in += 1
    else:
        count_out += 1
print('{} in' .format(count_in))
print('{} out' .format(count_out))