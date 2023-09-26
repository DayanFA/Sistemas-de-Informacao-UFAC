gr=1
gre = 0
i=0
g=0
e=0
while True:
    gre +=1
    gi,gg = map(int,input().split())
    if gi > gg:
        i +=1
    elif gg> gi:
        g +=1
    elif gi == gg:
        e +=1
    print('Novo grenal (1-sim 2-nao)')
    gr=int(input())
    if gr == 1:
        continue
    elif gr ==2:
        print(f'{gre} grenais')
        print(f'Inter:{i}')
        print(f'Gremio:{g}')
        print(f'Empates:{e}')
        if i > g:
            x = 'Inter'
        elif g > i:
            x = 'Gremio'
        print(f'{x} venceu mais')
        break