#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.

'''
nome = input()
media = int(input())

dicionario = dict()
dicionario = {nome : media}
'''
dicionario = dict()
dicionario = {input() : int(input())}

print(dicionario)