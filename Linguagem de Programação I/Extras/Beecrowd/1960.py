def int_to_roman(n):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i in range(len(values)):
        while n >= values[i]:
            n -= values[i]
            res += numerals[i]
    return res

N = int(input())
print(int_to_roman(N))