'''https://www.4devs.com.br/gerador_de_cpf'''

'''1- Coletar a soma dos 9 primeiros digitos do CPF, multiplicando cada um dos valores por uma contagem regressiva comecando do 10, somar todos os resultados dessa multiplicacao'''

cpf = '32216007552'
cpf_tratado = cpf.replace('.', '').replace('-', '').replace(' ', '')

#while cpf_tratado.isnumeric() is False:
#    print('Valores não numéricos!')
#    cpf = input('CPF: ')
#    cpf_tratado = cpf.replace('.', '').replace('-', '').replace(' ', '')


soma_9_digitos = 0
contador_1 = 10
for digito_1 in cpf_tratado:
    if contador_1 == 1:
        break
    
    digito_X_contador_1 = int(digito_1) * contador_1

    soma_9_digitos += digito_X_contador_1

    contador_1 -=1

'''2- Multiplicar o resultado anterior por 10'''

soma_9_digitos_X_10 = soma_9_digitos * 10

'''3- Obter o resto da divisao por 11 da conta anterior'''

resto_11_1 = soma_9_digitos_X_10 % 11

'''4- Se o resultado anterior > 9 --> 0. Senao --> resultado anterior'''

if resto_11_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_11_1

'''5- Para calcular o segundo digito, o processo e praticamente o mesmo, com a excecao de que o primeiro digito tem que ser incluido nas contas'''

soma_10_digitos = 0
contador_2 = 11
for digito_2 in cpf_tratado:
    if contador_2 == 1:
        break
    
    digito_X_contador_2 = int(digito_2) * contador_2

    soma_10_digitos += digito_X_contador_2

    contador_2 -=1

'''6- Multiplicar o resultado anterior por 10'''

soma_10_digitos_X_10 = soma_10_digitos * 10

'''7- Obter o resto da divisao por 11 da conta anterior'''

resto_11_2 = soma_10_digitos_X_10 % 11

'''8- Se o resultado anterior > 9 --> 0. Senao --> resultado anterior'''

if resto_11_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resto_11_2

'''9- Verificando se o cpf e valido'''

penultimo_digito_cpf_usuario = int(cpf_tratado[-2])
ultimo_digito_cpf_usuario = int(cpf_tratado[-1])

primeira_condicao = penultimo_digito_cpf_usuario == primeiro_digito
segunda_condicao = ultimo_digito_cpf_usuario == segundo_digito

if primeira_condicao and segunda_condicao:
    if cpf_tratado.count(cpf_tratado[0]) == 11:
        print(f'O CPF {cpf} é invalido!')
    else:
        print(f'O CPF {cpf} é valido!')
else:
    print(f'O CPF {cpf} é invalido!')