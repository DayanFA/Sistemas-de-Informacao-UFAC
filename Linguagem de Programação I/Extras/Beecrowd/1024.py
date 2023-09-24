n = int(input())
for _ in range(n):
    m = input()
    z = ""
    for i in m:
        if i.isalpha():
            z += chr(ord(i) + 3)
        else:
            z += i
    k = z[::-1]
    m = len(k) // 2
    a = k[:m]
    b = k[m:]
    b1 = []
    for j in b:
        k1 = ord(j) - 1
        a1 = chr(k1)
        b1.append(a1)
    r = ''.join(b1)
    c = a + r
    print(c)
