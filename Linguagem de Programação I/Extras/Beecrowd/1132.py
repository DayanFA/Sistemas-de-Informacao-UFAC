x = int(input())
y = int(input())
if x> y:
    y,x = x,y
r=0
for i in range (x, y+1):
    if i % 13 == 0:
        continue
    else:
        r += i
print(r)