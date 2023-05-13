# Defina a função div que recebe como argumentos dois números naturais  m  e  n  e 
# devolve o resultado da divisão inteira de  m  por  n . 

# div(7,2)
# Esperado: 3

def div(m, n):
    if n != 0:
        return print(m // n)
    else:
        print("Essa divisao nao existe")

x, y = map(int, input().split())
div(x, y)
