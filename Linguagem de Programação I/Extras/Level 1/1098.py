i = 0
j = 1
while i <= 2:
    for a in range(3):
        if i == 0 or i == 1 or i >= 1.9:
            print("I={} J={}".format(round(i), round(j)))
        else:
            print("I={} J={}".format(format(i, ".1f"), format(j, ".1f")))
        j += 1
    i += 0.2
    j += 0.2 - 3.0