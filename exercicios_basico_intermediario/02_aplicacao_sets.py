'''Criar uma funcao que encontra o primeiro duplicado considerando o segundo numero como a duplicacao. Retornar a duplicacao considerada. Requisitos:
1- A ordem do numero duplicado e considerada a partir da segunda ocorrencia do numero, ou seja, o numero duplicado em si.
2- Exemplos:
    [1, 2, 3, 3, 2, 1] --> Retornar 3
    [1, 2, 3, 4, 5, 6] --> Retornar -1 --> Sem duplicacoes'''

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrando_duplicatas(lista_composta):
    set_aux = set()
    lista_duplicados = []
    
    for lista in lista_composta:
        
        contador = 1
        for elemento in lista:
            if elemento not in set_aux:
                set_aux.add(elemento)
                contador += 1
            elif elemento in set_aux:
                lista_duplicados.append(elemento)
                set_aux.clear()
                break
            if contador == len(lista):
                lista_duplicados.append(-1)
    
    return lista_duplicados

resultado = encontrando_duplicatas(lista_de_listas_de_inteiros)

indice = 1
for numero in resultado:
    if numero == -1:
        print(f'A lista {indice} não apresentou valores duplicados.')
        indice += 1
    else:
        print(f'O número que se repetiu na lista {indice} foi {numero}')
        indice += 1