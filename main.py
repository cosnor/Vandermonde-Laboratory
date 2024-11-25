from functions import matriz_inversa, printear_matriz
from simbols import ecuacion


#Escriba el arreglo de puntos

puntos = [(1,2), (2,3), (3,5)]

## Extraigo los valores de x e y

x = [punto[0] for punto in puntos]

y = [punto[1] for punto in puntos]

## Creo la matriz de Vandermonde

n = len(x)
V = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        V[i][j] = x[i]**j


## Creo Matriz Inversa de Vandermonde

V_inversa = matriz_inversa(V)

## Multiplico V_inversa por matriz b (y)

resultado = [[0 for i in range(len(y))] for j in range(len(V_inversa))]
for i in range(len(V_inversa)):
        for j in range(len(y)):
            for k in range(len(V_inversa)):
                resultado[i][j] += V_inversa[i][k] * y[k]


## Muestra el polinomio

polinomio = ecuacion(resultado, x)
print(f"\nPolinomio: P(x) = {polinomio}")

polinomio.evaluar(x)