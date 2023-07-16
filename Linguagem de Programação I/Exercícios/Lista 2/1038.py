pc, q= map(int, input().split())
if pc == 1:
    tv = q * 4.00
elif pc == 2:
    tv = q * 4.50
elif pc == 3:
    tv = q * 5.00
elif pc == 4:
    tv = q * 2.00
elif pc == 5:
    tv = q * 1.50
else:
    tv = 0.00
print("Total: R$ {:.2f}".format(tv))