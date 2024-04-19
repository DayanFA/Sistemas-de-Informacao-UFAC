T = int(input().strip())

for _ in range(T):
    N = int(input().strip())

    names = input().strip().split()

    records = input().strip().split()

    absent_students = []

    for i in range(N):
        total_classes = records[i].count('P') + records[i].count('A')
        attendance_percentage = (records[i].count('P') / total_classes) * 100

        if attendance_percentage < 75:
            absent_students.append(names[i])

    print(' '.join(absent_students))