X = int(input())
Y = int(input())
if X > Y:
    X, Y = Y, X
sum_odd = 0
for num in range(X+1, Y):
    if num % 2 != 0:
        sum_odd += num
print(sum_odd)
