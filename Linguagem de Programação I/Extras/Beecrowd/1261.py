import sys

m, n = map(int, input().split())
dictionary = {}
for _ in range(m):
    word, value = input().split()
    dictionary[word] = int(value)
for _ in range(n):
    salary = 0
    while True:
        line = input()
        if line == '.':
            break
        for word in line.split():
            salary += dictionary.get(word, 0)
    print(salary)