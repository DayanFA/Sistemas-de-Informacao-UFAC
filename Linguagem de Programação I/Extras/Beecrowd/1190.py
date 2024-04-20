operation = input().strip()
matrix = []
sum_elements = 0
count_elements = 0

for i in range(12):
    matrix.append([])
    for j in range(12):
        value = float(input().strip())
        matrix[i].append(value)
        if i < 6 and j > 11 - i or i > 5 and j > i:
            sum_elements += value
            count_elements += 1

if operation == 'S':
    print("{:.1f}".format(sum_elements))
elif operation == 'M':
    print("{:.1f}".format(sum_elements / count_elements))