s = float(input())
if s <= 2000.00:
    print("Isento")
else:
    vtax = s - 2000.00
    if vtax <= 1000.00:
        tax = vtax * 0.08
    elif 1000.00 < vtax <= 2000.00:
        tax = 1000.00 * 0.08
        r = vtax - 1000.00
        tax += r * 0.18
    else:
        tax = 1000.00 * 0.08
        tax += 1500.00 * 0.18
        r = vtax - 2500.00
        tax +=  r * 0.28
    print("R$ {:.2f}".format(tax))