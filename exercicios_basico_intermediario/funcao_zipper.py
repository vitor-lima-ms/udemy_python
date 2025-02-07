'''Criar uma funcao que ira unir duas listas, mantendo a ordem, usando os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]'''

def zipper(list_01, list_02):
    
    max_range = min(len(list_01), len(list_02))
    
    aux_list = []
    main_list = []

    for index in range(0, max_range):
        aux_list.append(list_01[index])
        aux_list.append(list_02[index])
        main_list.append(tuple(aux_list))
        aux_list.clear()
    
    return main_list

resultado = zipper(
    ['BA', 'SP', 'MG', 'RJ'],
    ['Salvador', 'Ubatuba', 'Belo Horizonte'],
)

#print(resultado)

#Solucao do professor

def zipper(list_01, list_02):
    
    max_range = min(len(list_01), len(list_02))
    
    return [
        (list_01[index], list_02[index]) for index in range(0, max_range)
    ]

resultado = zipper(
    ['BA', 'SP', 'MG', 'RJ'],
    ['Salvador', 'Ubatuba', 'Belo Horizonte'],
)

#print(resultado)