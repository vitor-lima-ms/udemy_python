nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade is not None:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f"Seu nome tem {len(nome.replace(' ', ''))} letras")
    print(f'A última letra do seu nome é {nome[len(nome) - 1]}')
else:
    print('Desculpe, voce deixou campos vazios')