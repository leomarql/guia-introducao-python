#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

frase = input()
a = 0
primeira = 0
ultima = 0

for i in range(0, len(frase)-1):
    if frase[i] == 'a':
        a += 1
        if a == 1:
            primeira = i
        else: 
            ultima = i

''' O seguinte programa conta o número de vezes que a letra a aparece em uma string
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
'''

print('a letra A aparece {} vezes na frase digitada'.format(a))
print('A aparece pela primeira vez na posicao: {}'.format(primeira))
print('A aparece pela ultima vez na posicao: {}'.format(ultima))