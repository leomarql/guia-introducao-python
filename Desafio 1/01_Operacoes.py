# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a, b, c = map(int, input().split())

print('Soma entre os numeros: {}'.format(a + b + c))
print('Multiplicacao entre os numeros: {}'.format(a * b * c))
print('Divisao entre os numeros: {}'.format(a / b / c))

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.

x = int(input("Entre  a number: "))

print('Raiz quadrada do numero digitado: {}'.format(x ** 0.5))