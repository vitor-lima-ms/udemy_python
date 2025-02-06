#List e dict comprehension
from random import randint
lista = [
    randint(0, 10) 
    for indice in range(10)
] #Adiciona um numero aleatorio de 0 a 10 para cada numero no range(10). Ou seja, minha lista terá 10 número aleatórios
'''print('Original', lista)'''

#Mapping - lista
lista_map = [
    numero * 2 #Quero o numero da lista de cima x2
    if numero < 4 else numero #Se ele for menor que 4. Se nao, quero so o numero
    for numero in lista #Para cada numero da lista
]
'''print('Mapping:', lista_map)'''

#Filtering - lista
lista_filt = [
    numero
    for numero in lista
    if numero > 4
]
'''print('Filtering', lista_filt)'''

#Mapping, filtering e ordering em listas com dicionarios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(*produtos, sep='\n')

#Mapping
produtos_modificados = [ 
    {'nome': produto['nome'], 'preco': produto['preco'] * 1.25} #Aumento de 25% no preco
    for produto in produtos
]
print()
print(*produtos_modificados, sep='\n')

#Ordering
def ordena_por_nome(produto):
    return produto['nome']

produtos_ordenados_nome = sorted(produtos, key=ordena_por_nome)
print()
print(*produtos_ordenados_nome, sep='\n')

#Filtering
produtos_filtrados = [
    produto
    for produto in produtos
    if produto['preco'] > 11
]
print()
print(*produtos_filtrados, sep='\n')