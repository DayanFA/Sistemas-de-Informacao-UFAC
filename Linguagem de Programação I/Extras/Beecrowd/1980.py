import math

while True:
    S = input().strip()
    if S == '0':
        break

    print(math.factorial(len(S)))