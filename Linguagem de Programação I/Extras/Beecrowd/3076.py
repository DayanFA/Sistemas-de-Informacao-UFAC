import sys

for line in sys.stdin:
    year = int(line)
    century = (year + 99) // 100
    print(century)