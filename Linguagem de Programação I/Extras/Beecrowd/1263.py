while True:
    try:
        line = input().lower().split()
        count = 0
        prev = ''
        for i in range(len(line) - 1):
            if line[i][0] == line[i+1][0] and (i == 0 or line[i][0] != line[i-1][0]):
                count += 1
        print(count)
    except EOFError:
        break