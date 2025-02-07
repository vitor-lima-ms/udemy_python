'''Programa que pede o primeiro nome do usuario --> Se o nome tiver 4 letras ou menos == "Seu nome e curto" --> Se o nome tiver entre 5 e 6 letras == "Seu nome é normal" --> Se o nome tiver mais que 6 letras == "Seu nome e muito grande"'''

nome = input('Digite o seu nome: ')
while (nome.isnumeric() is True) or (nome.isalnum() is False) or (nome.isalpha() is False) or (len(nome) < 3):
    print('Nome inválido!')
    nome = input('Por favor, digite o seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')