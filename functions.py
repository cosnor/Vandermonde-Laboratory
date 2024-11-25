def printear_matriz(V):
    for i in range(len(V)):
        print(V[i])

def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for j in range(len(matriz)):
        submatriz = []
        for i in range(1, len(matriz)):
            fila = []
            for k in range(len(matriz)):
                if k != j:
                    fila.append(matriz[i][k])
            submatriz.append(fila)
        det += ((-1) ** j) * matriz[0][j] * determinante(submatriz)
    return det

def matriz_adjunta(matriz):
    n = len(matriz)
    adjunta = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Crear la submatriz eliminando fila i y columna j
            submatriz = []
            for k in range(n):
                if k != i:
                    fila = []
                    for l in range(n):
                        if l != j:
                            fila.append(matriz[k][l])
                    submatriz.append(fila)
            # Calcular el cofactor
            adjunta[j][i] = ((-1) ** (i + j)) * determinante(submatriz)
    
    return adjunta

def matriz_inversa(matriz):
    # Verificar si la matriz es cuadrada
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada")
    
    # Calcular el determinante
    det = determinante(matriz)
    
    # Verificar si la matriz es invertible
    if det == 0:
        raise ValueError("La matriz no es invertible (determinante = 0)")
    
    # Calcular la matriz adjunta
    adjunta = matriz_adjunta(matriz)
    
    # Calcular la inversa (adjunta / determinante)
    n = len(matriz)
    inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]
    
    return inversa