import copy

matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_B = [[10], [20], [30]]

matrizes = [
    [[matriz_B[i][0] if j == c else val for j, val in enumerate(linha)] for i, linha in enumerate(matriz_A)]
    for c in range(3)
]

"""
matrizes = []

for c in range(3):
    matriz_C = copy.deepcopy(matriz_A)
    for indiceL, linha in enumerate(matriz_C):
        linha[c] = matriz_B[indiceL][0]
    matrizes.append(matriz_C)

matriz_A1, matriz_A2, matriz_A3 = matrizes
"""

def imprimirMatriz(matriz):
    for linha in matriz:
        for indice in linha:
            print(f"[{indice}]", end="")
        print("")
    
    print("-"*17)


imprimirMatriz(matriz_A1)
imprimirMatriz(matriz_A2)
imprimirMatriz(matriz_A3)
