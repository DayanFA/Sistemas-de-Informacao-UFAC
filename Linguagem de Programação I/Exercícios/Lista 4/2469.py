N = int(input())
grades = list(map(int, input().split()))

grade_count = {}
for grade in grades:
    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1

most_frequent_grade = None
highest_frequency = 0

for grade, frequency in grade_count.items():
    if frequency > highest_frequency or (frequency == highest_frequency and grade > most_frequent_grade):
        most_frequent_grade = grade
        highest_frequency = frequency

print(most_frequent_grade)