import re

N = int(input())
for _ in range(N):
    line = input()
    line = re.sub(r'\b[a-zA-Z]oulupukk[a-zA-Z]\b', 'Joulupukki', line)
    print(line)