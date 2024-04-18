operation = input()
matrix = []

for _ in range(12):
    matrix.append([float(input()) for _ in range(12)])

if operation == 'S':
    result = sum(matrix[i][j] for i in range(12) for j in range(i+1, 12))
else:
    result = sum(matrix[i][j] for i in range(12) for j in range(i+1, 12)) / 66

print('{:.1f}'.format(result))