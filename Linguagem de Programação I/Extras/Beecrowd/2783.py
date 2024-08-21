N, C, M = map(int, input().split())
figurinhas_carimbadas = set(map(int, input().split()))
figurinhas_compradas = list(map(int, input().split()))

figurinhas_carimbadas_compradas = set()
for figurinha in figurinhas_compradas:
    if figurinha in figurinhas_carimbadas:
        figurinhas_carimbadas_compradas.add(figurinha)

figurinhas_faltantes = figurinhas_carimbadas - figurinhas_carimbadas_compradas

print(len(figurinhas_faltantes))