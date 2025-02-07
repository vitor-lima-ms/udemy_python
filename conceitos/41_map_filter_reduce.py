#map --> Mapear dados --> Mesma coisa que a gente fez com list comprehension --> Mas precisamos criar uma funcao somente com o que estaria entre chaves no caso de um list comprehension de listas com dicionarios dentro

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumento(produto):
    return {
        **produto, 'preco': round(produto['preco'] * 1.1, 2)
    }

novos_produtos = map( #A funcao itera sobre cada elemento do objeto iteravel (nesse caso os produtos da lista produtos) e aplica a funcao por mim definida
    aumento,
    produtos
)

#print(*list(novos_produtos), sep='\n')

#filter --> FIltrar dados --> Mesma coisa que a gente fez com list comprehension --> Mas precisamos criar uma funcao --> Pode ser uma lambda

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''def filtrar(produto):
    return produto['preco'] > 11''' #Poderia usar essa ao inves da lambda

produtos_filtrados = filter(
    lambda produto: produto['preco'] > 11,
    produtos
)

#print(*list(produtos_filtrados), sep='\n')

#reduce --> Utilizada para reduzir iteraveis em um unico valor --> Somar todos os valores por exemplo

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def redutora(acumulador, produto):
    #print(acumulador, produto) #So pra entender a logica
    return round(acumulador + produto['preco'], 2)

soma_precos = reduce(
    redutora,
    produtos,
    0 #Importante colcoar pra evitar erros. Esse e o valor inicial que a funcao reduce considera para o acumulador da funcao redutora. Se nao passassemos ele, a reduce consideraria o primeiro produto como o valor inicial do acumulador
)

'''soma_precos = reduce(
    lambda accum, produto: accum + produto['preco'], #Da pra fazer com lambda tambem
    produtos,
    0
)'''

print(soma_precos)