N = int(input())

for _ in range(N):
    T = int(input())
    if T < 2015:
        print(f"{2015 - T} D.C.")
    elif T == 2015:
        print("1 A.C.")
    else:
        print(f"{T - 2014} A.C.")