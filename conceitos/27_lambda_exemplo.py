produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''Ordenar os produtos por preco crescente e gerar uma variavel produtos_ordenados_por_preco por deep copy'''

ordenamento = sorted(produtos, key=lambda produto: produto['preco'])

from copy import deepcopy

produtos_ordenados_por_preco = deepcopy(ordenamento)

print(*produtos_ordenados_por_preco, sep='\n')