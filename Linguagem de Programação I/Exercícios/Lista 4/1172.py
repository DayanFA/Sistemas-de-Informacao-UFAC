X = []
for i in range(10):
    num = int(input())
    X.append(num)

for i in range(10):
    if X[i] <= 0:
        X[i] = 1

for i in range(10):
    print("X[{}] = {}".format(i, X[i]))