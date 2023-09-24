c=0
while c!=2:
    n = float(input())
    if n<0:
        print('nota invalida')
    elif n > 10:
        print('nota invalida')
    elif n>=0:
        c+=1
        x1=n
    if c== 1:
        x2=x1
    if c== 2:
        m=(x1+x2)/2.0
        print('media = {:.2f}' .format(m))