#Combinacao --> Ordem dos items agrupados nao importa --> Iteravel + tamanho do grupo
#Permutacao --> Ordem dos items importa
#Produto

import itertools

pessoas = [
    'Joao', 'Joana', 'Luiz', 'Leticia'
]
camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g'],
    ['Masc.', 'Fem.'],
]

combinacao = list(itertools.combinations(pessoas, 2)) #Combinacao em grupos de 2
#print(*combinacao, sep='\n')

permutacao = list(itertools.permutations(pessoas, 2))
#print(*permutacao, sep='\n')

produto = list(itertools.product(*camisetas)) #Temos que desempacotar antes
print(*produto, sep='\n')