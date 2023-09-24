f = input()
v = {}
for i in f:
    i = i.lower()
    l = "aeiou"
    if i in l:
        if i in v:
            v[i] += 1
        else:
            v[i] = 1
print(v)


