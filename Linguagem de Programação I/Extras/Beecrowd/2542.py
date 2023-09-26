while True:
    try:
        n = int(input())
        m, l = map(int,input().split())
        cm= []
        cl= []
        li = []
        for i in range(m):
            li = list(map(int, input().split()))
            cm.append(li)
        for i in range(l):
            li = list(map(int, input().split()))
            cl.append(li)
        cm2, cl2 = map(int, input().split())
        at = int(input())
        if cm[cm2-1][at-1] == cl[cl2-1][at-1]:
            print('Empate')
        elif cm[cm2-1][at-1] > cl[cl2-1][at-1]:
            print('Marcos')
        else:
            print('Leonardo')
    except EOFError:
        break