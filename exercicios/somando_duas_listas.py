'''Some os valores de duas listas compostas apenas de inteiros ou floats. Se uma lista for maior do que a outra, a soma so vai considerar o tamanho da menor'''

list00 = [1, 2, 3, 4, 5, 6, 7]
list01 = [1, 2, 3, 4]

merge_list = list(zip(list00, list01))

final_list = [
    sum(item) for item in merge_list
]

print(final_list)