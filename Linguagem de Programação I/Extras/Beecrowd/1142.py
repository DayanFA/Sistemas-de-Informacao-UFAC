n = int(input())
for i in range(n*4):
    i +=1
    k= i
    if i % 4 == 0:
        k= 'PUM'
        print(k)
    else:
        print('{}'.format(i), end=' ')