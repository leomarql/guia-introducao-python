# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 
def numeroPrimo (a):
    primo = True
    
    for i in range(2, a):
        if a % i == 0:
            primo = False

    if primo:
        return print('{} eh primo'.format(a))
    else:
        return print('{} nao eh primo'.format(a))

numero = int(input())
numeroPrimo(numero)