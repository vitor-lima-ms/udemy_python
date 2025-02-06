'''def fora(x):
    a = x #Variavel livre -> Nao esta definida dentro do escopo da funcao de dentro
    
    def dentro():
        return a
    
    return dentro

dentro1 = fora(10) #A variavel dentro recebe a funcao fora, que retorna a funcao dentro
dentro2 = fora(20) #A variavel dentro recebe a funcao fora, que retorna a funcao dentro
print(dentro1()) #Retorna a = x = 10
print(dentro2()) #Retorna a = x = 20'''

###

'''def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        valor_final += valor_a_concatenar #Erro --> pq o valor_final nao esta no escopo da funcao de dentro --> Temos que informar ao Python para buscar o valor dessa variavel no escopo da funcao de fora
        return valor_final
    
    return interna'''

###

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar=''):
        nonlocal valor_final #Temos que usar o nonlocal pra corrigir o erro que dava no codigo de cima
        valor_final += valor_a_concatenar 
        return valor_final
    
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c() #Funcao que lembra o valor de uma variavel
print(final)