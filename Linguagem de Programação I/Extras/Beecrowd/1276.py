while True:
    try:
        s = sorted(set(input().replace(' ', '')))
        ranges = []
        if s:
            start = end = s[0]
            for c in s[1:]:
                if ord(c) - ord(end) > 1:
                    ranges.append(f'{start}:{end}')
                    start = c
                end = c
            ranges.append(f'{start}:{end}')
        print(', '.join(ranges))
    except EOFError:
        break