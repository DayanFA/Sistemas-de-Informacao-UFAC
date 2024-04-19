date = input().strip()

day, month, year = date.split('/')

print(f"{month}/{day}/{year}")
print(f"{year}/{month}/{day}")
print(f"{day}-{month}-{year}")