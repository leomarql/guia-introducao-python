#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''REVISAR DEPOIS'''

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')

for fruta in frutas:
    print('Vogais da palavra', fruta + ': ', end='')
    vogais = []
    for letra in fruta:
        if letra in "aeiou" and letra not in vogais:
            vogais.append(letra)
    print(', '.join(vogais))