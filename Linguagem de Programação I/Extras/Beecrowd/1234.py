while True:
    try:
        a = input()
        b = ""
        m= True
        for i in a:
            if i.isalpha():
                if m:
                    b += i.upper()
                else:
                    b += i.lower()
                m = not m
            else:
                b += i
        print(b)
    except EOFError:
        break