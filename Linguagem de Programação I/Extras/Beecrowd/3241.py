N = int(input())

for _ in range(N):
    line = input().strip()
    if line == "P=NP":
        print("skipped")
    else:
        a, b = map(int, line.split("+"))
        print(a + b)