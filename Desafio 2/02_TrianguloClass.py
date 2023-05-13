# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.

x, y, z = map(int, input().split())

triangulo = False

if (x > abs(y - z) and x < y + z and y > abs(x - z) and y < x + z and z > abs(x - y) and z < x + y):
    if x == y == z:
        print('X, Y e Z formam um triangulo equilatero')
        
    elif x == y or x == z or y == z:
        print('X, Y e Z formam um triangulo isosceles')
        
    else:
        print('X, Y e Z formam um triangulo escaleno')
        
else:
    print('X, Y e Z nao formam um triangulo')   