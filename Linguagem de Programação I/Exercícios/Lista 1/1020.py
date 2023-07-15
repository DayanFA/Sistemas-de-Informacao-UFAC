ad=int(input())
y= ad//365
ad = ad%365
m=ad//30
ad= ad%30
d= ad
print('{} ano(s)'.format(y))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))