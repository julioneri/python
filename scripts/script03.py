import copy

matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_B = [[10], [20], [30]]

matrizes_C = []
for c in range(3):
    matriz_C = copy.deepcopy(matriz_A)

    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL][0]

    matrizes_C.append(matriz_C)

matriz_C1, matriz_C2, matriz_C3 = matrizes_C

print("MATRIZ_PRINCIPAL:")
for c in matriz_A:
    print(f'{c}')
    print("")

print("-"*17)

print("MATRIZ_C1:")
for c in matriz_C1:
    print(f'{c}')
    print("")

print("-"*17)

print("MATRIZ_C2:")
for c in matriz_C2:
    print(f'{c}')
    print("")

print("-"*17)

print("MATRIZ_C3:")
for c in matriz_C3:
    print(f'{c}')
    print("")

print("-"*17)
