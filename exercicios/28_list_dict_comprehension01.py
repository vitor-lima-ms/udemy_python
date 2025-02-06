produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''Aumentar o preco dos produtos em 10% e gerar uma variavel novos_produtos por deep copy'''

aumento = [
    {'nome': produto['nome'], 'preco': round((produto['preco'] * 1.1), 2)}
    for produto in produtos
]

from copy import deepcopy

novos_produtos = deepcopy(aumento)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')