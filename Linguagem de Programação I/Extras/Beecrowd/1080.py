highest_number = 0
highest_position = 0

for i in range(1, 101):
    num = int(input())

    if num > highest_number:
        highest_number = num
        highest_position = i

print(highest_number)
print(highest_position)