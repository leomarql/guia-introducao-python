import numpy as np

#1- Crie uma matriz 1D com números de 0 a 9
arr = np.arange(10) #CRIA UMA MATRIZ 1D COM 10 PARAMETROS, DE 0 A 9 
print(arr)

#2- Crie uma matriz booleana numpy 3×3 com ‘True’
bool_arr = np.full((3, 3), True, dtype = bool)
print(bool_arr)

#3- Extraia todos os números ímpares de ‘arr’

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

num_impares = []

for i in range(0, 10):
    if arr[i]%2 != 0:
        num_impares.append(arr[i])

print(num_impares)

#4- Substitua todos os números ímpares arr por -1
for i in range(0, 10):
    if i % 2 != 0:
        arr[i] = -1

print(arr)

#5- Substitua todos os números ímpares em arr com -1 sem alterar arr

arr = np.arange(10)
out = np.where(arr % 2 != 0, -1, arr)

print(arr)
print(out)

#6- Converta uma matriz 1D para uma matriz 2D com 2 linhas:

arr = np.arange(10)
print(arr)

arr = arr.reshape(2, -1)
print(arr)

#6- Empilhe matrizes verticalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
matriz_vertical = np.vstack((a, b))
print(matriz_vertical)

#6- Empilhe as matrizes horizontalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
matriz_horizontal = np.hstack((a, b))
print(matriz_horizontal)
