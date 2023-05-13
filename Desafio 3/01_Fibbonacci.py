# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.

'''
Formula de fibonacci: F(n+2) = F(n+1) + F(n)
'''
n1 = 0
n2 = 1
i = 1

''' USANDO WHILE

while i <= 10:
    if i == 1:
        print('n{} = {}'.format(i, n1))
        i += 1
    elif i == 2:
        print('n{} = {}'.format(i, n2))
        i += 1
    else:
        n = n2 + n1
        print('n{} = {}'.format(i, n))
        
        n1 = n2
        n2 = n
        i += 1 
 '''

''' USANDO FOR 
com o for, i começa em 1 e vai até 10, ou seja, para quando chega no 11. 
não é preciso fazer i += 1 pq o próprio for já faz isso
'''  
for i in range(1, 11): 
    if i == 1:
        print('n{} = {}'.format(i, n1))
    elif i == 2:
        print('n{} = {}'.format(i, n2))
    else:
        n = n2 + n1
        print('n{} = {}'.format(i, n))
        
        n1 = n2
        n2 = n