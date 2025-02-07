'''def add_clients(name, list_=[]):
    list_.append(name)
    return list_

clients_list00 = add_clients('Vitor')
add_clients('João', clients_list00)

clients_list01 = add_clients('Ana')
add_clients('Maria', clients_list01)

print(clients_list00)
print(clients_list01) #Problema --> Python adicionou todos os nomes na mesma lista --> Toda vez que nao passamos um parametro opcional que seja mutavel, o Python reutilizara esse tipo mutavel'''

#Resolucao do problema

def add_clients(name, list_=[]):
    list_.append(name)
    return list_

list00 = []
clients_list00 = add_clients('Vitor', list00)
add_clients('João', clients_list00)

clients_list01 = add_clients('Ana')
add_clients('Maria', clients_list01)

print(clients_list00)
print(clients_list01) #Dessa vez, o Python nao adicionou todos os nomes na mesma lista pois passamos uma lista como argumento na primeira chamada da funcao

#A melhor maneira de evitar isso e nao passar tipos mutaveis como valores padrao de parametros de funcao