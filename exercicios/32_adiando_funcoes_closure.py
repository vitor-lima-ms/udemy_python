'''Adiando a execucao de funcoes'''

'''#Minha solucao

def soma(x, y):
   return x + y

def multiplica(x, y):
    return x * y

def cria_funcao(funcao, *args):
    args_lista = list(args)
    y = int(input('Digite o y: '))
    args_lista.append(y)
    return funcao(*args_lista)

soma_com_5 = cria_funcao(soma, 5)
multiplica_por_10 = cria_funcao(multiplica, 10)

print(soma_com_5)
print(multiplica_por_10)'''

#Solucao do prof - Utilizou closure

def soma(x, y):
   return x + y

def multiplica(x, y):
    return x * y

def cria_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_5 = cria_funcao(soma, 5)
multiplica_por_10 = cria_funcao(multiplica, 10)

print(soma_com_5(2))
print(multiplica_por_10(2))