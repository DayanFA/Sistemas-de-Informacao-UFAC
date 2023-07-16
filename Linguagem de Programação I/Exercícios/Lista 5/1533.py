while True:
    N = int(input())
    if N == 0:
        break
    
    sus = list(map(int, input().split()))
    secmsus = max(sus)
    msus = -1
    
    for sup in sus:
        if sup != secmsus:
            msus = max(msus, sup)
    
    k = sus.index(msus) + 1
    print(k)