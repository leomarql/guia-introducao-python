# Escreva uma função para encontrar o maior entre 3 numeros

def Max(a,b,c):
    '''Uma das formas é usando a funcao padrao max() do pyhton
    
        return max(a, b, c)
    '''
    
    '''Construindo a funcao manualmente (pode ser melhorada)
    if(a > b):
        if(a > c):
            return a
        else:
            return c
    elif(b > c):
        return b
    else:
        return c
    '''
    return max(a, b, c)
    
x, y, z = map(int, input().split())

print('O maior numero é:', Max(x, y, z))