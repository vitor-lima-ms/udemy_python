#Temos que tratar os dados antes de usar

from itertools import groupby

exemplo = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']

agrupamento = groupby(exemplo)

for chaves, valores in agrupamento: #Retorna uma lista com o valor que ele utilizou para agrupar e os valores desse grupo em um objeto iteravel. Para acessar os valores do objeto iteravel, podemos usar o list()
    '''print(chaves, end='', flush=True)
    print(list(valores))'''

#Situacao mais complexa
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

'''def agrupamento(aluno):
    return aluno['nota']''' #Poderia utilizar essa funcao ao inves da lambda

alunos_deepcopy = deepcopy(alunos)
alunos_deepcopy.sort(key=lambda aluno: aluno['nota'])

alunos_ordenados_nota = groupby(alunos_deepcopy, key=lambda aluno: aluno['nota'])

for chaves, valores in alunos_ordenados_nota:
    print(chaves)
    print(*list(valores), sep='\n')