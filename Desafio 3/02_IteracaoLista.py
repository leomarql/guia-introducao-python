# Faça um programa que receba 5 números e retorne o maior e o menor numero, a soma e a média dos números.

lista = [1,77,87,-5, 10]

'''
maior = 0
menor = 0
soma = 0

for i in range (0, 5):
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
    
    soma += lista[i]

media = soma / 5.0
'''

'''usando funções de listas'''
maior = max(lista)
menor = min(lista)
soma = sum(lista)
media = soma / len(lista)

print('maior numero: {}'.format(maior))
print('menor numero: {}'.format(menor))
print('soma dos numeros: {}'.format(soma))
print('media dos numeros: {}'.format(media))
