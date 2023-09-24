n = int(input())
mat = []
dif=[]
r = []
for i in range(n):
    linha = list(map(int,input().split()))
    mat.append(linha)
for j in range(n*2):
    k, l = map(int,input().split())
    dif.append(mat[k-1][l-1])
    r = list(set(dif))
print(len(r))