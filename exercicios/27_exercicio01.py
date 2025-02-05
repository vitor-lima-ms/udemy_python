'''Funcao que multiplica todos os argumentos nao nomeados recebidos e retorna esse valor'''

def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

X = multiplicacao(1, 2, 3, 4, 5)
print(X)