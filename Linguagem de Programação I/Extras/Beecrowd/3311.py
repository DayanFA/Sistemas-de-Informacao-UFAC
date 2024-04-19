N = int(input())
names = [input() for _ in range(N)]
names.sort(key=lambda name: name[0])
for name in names:
    print(name)