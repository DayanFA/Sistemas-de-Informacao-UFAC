n1,n2,n3,n4 = map(float, input().split())
m= (n1*2+n2*3+n3*4+n4*1)/10
print('Media: {:.1f}' .format(m))
if m >= 7.0:
    print("Aluno aprovado.")
elif m < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    s = float(input())
    print("Nota do exame: {}" .format(s, ".1f"))
    fm = (m + s) / 2
    if fm >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {}" .format(fm, ".1f"))