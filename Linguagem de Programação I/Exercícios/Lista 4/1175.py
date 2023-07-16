N = []
for i in range(20):
    num = int(input())
    N.append(num)

for i in range(10):
    N[i], N[19-i] = N[19-i], N[i]

for i in range(20):
    print("N[{0}] = {1}".format(i, N[i]))