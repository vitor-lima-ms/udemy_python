'''Fazer uma lista de compra com listas. O usuario deve ter a possibilidade de inserir, apagar e listar valores da lista. Nao permitir que o programa quebre com erros de indices inexistentes na lista'''

lista_compras = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar ou [s]air: ')

    if opcao not in 'IiAaLlSs':
        print('Opção inválida!')
        continue

    if opcao in 'Ss':
        break

    elif opcao in 'Ii':
        item = input('O que você deseja adicionar? ')
        
        while (item.isnumeric() is True) or (item.isalnum() is False) or (item.isalpha() is False):
            print('Item inválido!')
            item = input('O que você deseja adicionar? ')
        
        lista_compras.append(item)
    
    elif opcao in 'Aa':
        indice_apagar = input('Qual indice você deseja apagar? ')   

        while indice_apagar.isnumeric() is False:
            print('Por favor, digite um índice inteiro!')
            indice_apagar = input('Qual indice você deseja apagar? ')
        
        try:
            lista_compras.pop(int(indice_apagar))
        except IndexError:
            print('Esse índice não existe na lista!')

    else:
        print('-' * len('Listagem de itens'))
        print('Listagem de itens')
        print('-' * len('Listagem de itens'))
        for indice, item in enumerate(lista_compras):
            print(indice, item)