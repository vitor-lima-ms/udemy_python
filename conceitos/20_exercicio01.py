'''Programa que pede para o usuario digitar um numero inteiro e informar se ele e par. Caso o usuario digite um numero que nao e inteiro, informar que o numero nao e inteiro'''

num_str = input('Digite um numero inteiro: ')
while num_str.isnumeric() is False:
    print('Isso não é número inteiro!')
    num_str = input('Por favor, digite um numero inteiro: ')
num_int = int(num_str)
if (num_int % 2) == 0:
    print(f'O número {num_int} é par.')
else:
    print(f'O numero {num_int} não é par.')