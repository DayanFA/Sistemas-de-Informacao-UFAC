import sys

results = []
sum = 0
for line in sys.stdin:
    line = line.strip()
    if line == "caw caw":
        results.append(sum)
        sum = 0
    else:
        sum += int(line.replace('-', '0').replace('*', '1'), 2)
for result in results:
    print(result)