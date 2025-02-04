'''Programa que pede a hora e sauda o usuario conforme o horario --> Bom dia (0-11), Boa tarde (12-17) e Boa noite (18-23)'''

horario_str = input('Informe o horário: ')

while True:
    if horario_str.isnumeric() is True:
        if 0 <= int(horario_str) <= 24:
            break
    print('Esse não é um horário válido!')
    horario_str = input('Por favor, informe um horário válido: ')

horario_int = int(horario_str)

if 0 <= horario_int <= 11:
    print('Bom dia!')
elif 12 <= horario_int <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')