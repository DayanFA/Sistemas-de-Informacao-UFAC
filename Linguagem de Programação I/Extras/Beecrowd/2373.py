N = int(input().strip())
total_broken_cups = 0

for _ in range(N):
    L, C = [int(x) for x in input().strip().split(' ')]
    if L > C:
        total_broken_cups += C

print(total_broken_cups)