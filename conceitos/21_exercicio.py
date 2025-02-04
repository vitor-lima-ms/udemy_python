nome = 'Vitor Lima'

contador = 0
tamanho_nome = len(nome)
novo_nome = '*'

while contador < len(nome):
    novo_nome += f'{nome[contador]}*'
    contador += 1

print(novo_nome)