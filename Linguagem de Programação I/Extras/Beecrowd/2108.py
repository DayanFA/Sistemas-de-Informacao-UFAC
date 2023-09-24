m =0
b=""
while True:
    s = input()
    c= 0
    v = ''
    if s == '0':
        break
    k = s.split()
    for i in k:
        c = len(i)
        v += str(c) + "-"
        if c >= m:
            m = c
            b = i
    v = v[:-1]
    print(v)
print()
print("The biggest word: {}".format(b))