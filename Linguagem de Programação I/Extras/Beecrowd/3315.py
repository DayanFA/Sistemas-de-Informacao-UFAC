max_weekly_access = 0
for _ in range(4):
    weekly_access = sum(map(int, input().split()))
    if weekly_access > max_weekly_access:
        max_weekly_access = weekly_access

print(f"{max_weekly_access} = {bin(max_weekly_access)[2:]}")