mn = int(input())
m = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
mi = mn - 1
if 1 <= mn <= 12:
    mn = m[mi]
    print(mn)