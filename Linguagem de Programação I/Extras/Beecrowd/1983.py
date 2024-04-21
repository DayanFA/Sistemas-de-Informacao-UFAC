n = int(input())

maior_nota = -1
matricula_maior_nota = -1

for _ in range(n):
    matricula, nota = map(float, input().split())
    matricula = int(matricula)
    if nota > maior_nota:
        maior_nota = nota
        matricula_maior_nota = matricula

if maior_nota >= 8:
    print(matricula_maior_nota)
else:
    print("Minimum note not reached")