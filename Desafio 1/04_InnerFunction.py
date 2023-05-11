# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor

def funcao_externa(a, b):
    def funcao_interna():
        return a + b
    
    return funcao_interna() + 5

x, y = map(int, input().split())

print('resultado:', funcao_externa(x, y))