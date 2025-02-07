'''Funcao que retorna se um numero e par ou nao'''

def par(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Impar'

resultado = par(2)
print(resultado)
resultado = par(3)
print(resultado)
resultado = par(15)
print(resultado)
resultado = par(16)
print(resultado)