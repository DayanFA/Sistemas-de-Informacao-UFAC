F1 = float(input().strip())
F2 = float(input().strip())

total_fluctuation = (1 + F1 / 100) * (1 + F2 / 100) - 1

print(f'{total_fluctuation:.6f}')