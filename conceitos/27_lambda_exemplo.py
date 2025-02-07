#Ordering
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

''''''
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
#Os dados precisam estar ordenados

from copy import deepcopy
from itertools import groupby

alunos_deepcopy = deepcopy(alunos)
alunos_deepcopy.sort(key=lambda aluno: aluno['nota']) #Ordenamento

alunos_ordenados_nota = groupby(alunos_deepcopy, key=lambda aluno: aluno['nota']) #Agrupamento

for chaves, valores in alunos_ordenados_nota:
    print(chaves)
    print(list(valores))