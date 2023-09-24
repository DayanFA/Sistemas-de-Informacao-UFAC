while True:
    x,y = map(float, input().split())
    if x== y:
        break
    elif x> y:
        print("Decrescente")
    elif x<y:
        print("Crescente")