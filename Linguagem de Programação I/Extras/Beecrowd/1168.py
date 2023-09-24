n = int(input())
l=[6,2,5,5,4,5,6,3,7,6]
for _ in range(n):
    v=input()
    c=0
    for i in v:
        c +=l[int(i)]
    print('{} leds'.format(c))