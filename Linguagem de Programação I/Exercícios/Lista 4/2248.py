testSet = 1

while True:
    N = int(input())

    if N == 0:
        break

    students = []
    highestAverage = 0

    for _ in range(N):
        code, average = map(int, input().split())
        students.append((code, average))

        if average > highestAverage:
            highestAverage = average

    print("Turma", testSet)
    for code, average in students:
        if average == highestAverage:
            print(code, end=" ")
    print("\n")

    testSet += 1