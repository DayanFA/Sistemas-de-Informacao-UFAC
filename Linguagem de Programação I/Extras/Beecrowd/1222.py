import sys

for line in sys.stdin:
    n, l, c = map(int, line.split())
    words = input().split()
    lines = chars = pages = 0
    for word in words:
        if chars + len(word) > c:
            chars = 0
            lines += 1
            if lines == l:
                lines = 0
                pages += 1
        chars += len(word) + 1
    if chars or lines:
        pages += 1
    print(pages)