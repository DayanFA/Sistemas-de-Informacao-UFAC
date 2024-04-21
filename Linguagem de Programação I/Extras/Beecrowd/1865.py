C = int(input())
for _ in range(C):
    name, force = input().split()
    force = int(force)
    if name == "Thor":
        print('Y')
    else:
        print('N')