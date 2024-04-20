par = [0] * 5
impar = [0] * 5
c_par = c_impar = 0
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        par[c_par] = num
        c_par += 1
        if c_par == 5:
            for i in range(5):
                print(f'par[{i}] = {par[i]}')
            c_par = 0
    else:
        impar[c_impar] = num
        c_impar += 1
        if c_impar == 5:
            for i in range(5):
                print(f'impar[{i}] = {impar[i]}')
            c_impar = 0
for i in range(c_impar):
    print(f'impar[{i}] = {impar[i]}')
for i in range(c_par):
    print(f'par[{i}] = {par[i]}')