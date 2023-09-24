v = []
while True:
    try:
        v.append(input())
    except EOFError:
        break
v = set(v)
print(len(v))