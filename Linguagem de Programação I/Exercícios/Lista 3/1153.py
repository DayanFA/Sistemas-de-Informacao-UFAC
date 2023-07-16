def fat(n):
    if n==1:
        return 1
    return n*fat(n-1)
n = int(input())
r=fat(n)
print(r)