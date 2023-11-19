l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
val = list(filter(lambda x: x in l2, l1))
print(val)
