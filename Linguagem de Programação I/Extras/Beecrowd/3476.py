S, B, C = map(int, input().split())
total_time = 1 / (1/S + 1/B + 1/C)
print(f'{total_time:.3f}')