#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

nome = input()

def tem_silva(nome):
    silva = 'Silva'
    if silva in nome:
        print('tem Silva no nome')
    else: 
        print('nao tem Silva no nome')

tem_silva(nome)