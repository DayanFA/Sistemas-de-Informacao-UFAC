a,c, x, y = map(int, input().split())
pc = c-x-y-1
if pc >= a:
    print('Igor feliz!')
elif x> y/2:
    print('Caio, a culpa eh sua!')
else:
    print('Igor bolado!')