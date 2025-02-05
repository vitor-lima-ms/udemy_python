'''Qual letra aparece mais vezes em uma frase?'''

frase = 'O Python é uma linguagem de programacao multiparadigma. Python foi criado por Guido van Rossum'

frase_padronizada = frase.lower().replace(' ', '').replace('.', '')
i = 0
lista_letra_mais_vezes = []
letra_mais_vezes = ''
mais_vezes = 0

while i < len(frase_padronizada):
    letra = frase_padronizada[i]    
    vezes = frase_padronizada.count(letra)

    if vezes > mais_vezes:
        if i == 0:        
            lista_letra_mais_vezes.append(letra)
            lista_letra_mais_vezes.append(vezes)
            mais_vezes = vezes
        
        else:
            lista_letra_mais_vezes.pop()
            lista_letra_mais_vezes.pop()
            lista_letra_mais_vezes.append(letra)
            lista_letra_mais_vezes.append(vezes)
            mais_vezes = vezes

    elif vezes == mais_vezes:
        for elemento in lista_letra_mais_vezes:
            if elemento == letra:
                break

            elif lista_letra_mais_vezes.count(letra) < 1:
                lista_letra_mais_vezes.append(letra)
                lista_letra_mais_vezes.append(vezes)

    i += 1

if len(lista_letra_mais_vezes) == 2:
    print(f'A letra que mais aparece na frase é "{lista_letra_mais_vezes[0]}". Essa letra aparece {lista_letra_mais_vezes[1]} vezes.')

elif len(lista_letra_mais_vezes) > 2:
     print(f'As letras que mais aparecem na frase são "{lista_letra_mais_vezes[0::2]}". Essas letras aparecem {lista_letra_mais_vezes[1]} vezes.')