Xm, Ym, Xr, Yr = map(int, input().split())
crossings = abs(Xm - Xr) + abs(Ym - Yr)
print(crossings)