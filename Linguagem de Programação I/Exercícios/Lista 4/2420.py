N = int(input())
sections = list(map(int, input().split()))

total_length = sum(sections)

partial_sum = 0
for i in range(N):
    partial_sum += sections[i]
    if partial_sum == total_length - partial_sum:
        division_section = i + 1
        break

print(division_section)