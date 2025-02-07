'''Sistema de perguntas e resposta'''

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for indice in range(0, len(perguntas)):
    print(f'{perguntas[indice]["Pergunta"]}')
    
    contador = 0
    for opcoes in perguntas[indice]['Opções']:
        print(f'{contador})', opcoes)
        contador += 1
    
    resposta = input('Escolha uma opção: ')
    while (resposta not in '0123') and (resposta.isnumeric() is False):
        print('Opção inválida!')
        resposta = input('Escolha uma opção: ')

    if perguntas[indice]["Resposta"] == perguntas[indice]['Opções'][int(resposta)]:
        print('Parabéns, você acertou!')
        acertos += 1
    else:
        print('Que pena! Você errou.')

print(f'Você teve {acertos} acerto(s) no total!')