#Funcao zip

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

resultado = zip(l1, l2)

#print(list(resultado))

#Modulo itertools

from itertools import zip_longest #Utiliza o tamanho da maior lista ao inves da menor

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

resultado = zip_longest(l1, l2, fillvalue='Sem informação')

print(list(resultado))