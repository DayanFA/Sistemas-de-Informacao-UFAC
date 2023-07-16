N = int(input())

engine_rpm = list(map(int, input().split()))

fall_index = 0
for i in range(1, N):
    if engine_rpm[i] < engine_rpm[i-1]:
        fall_index = i + 1
        break

print(fall_index)