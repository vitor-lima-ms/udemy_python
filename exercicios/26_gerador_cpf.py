from random import randint

cpf_gerado_9_digitos = ''

for indice in range(0,9):
    num_aleatorio = randint(0, 9)
    str_num_aleatorio = str(num_aleatorio)
    cpf_gerado_9_digitos += str_num_aleatorio

#Gerando o penultimo digito

soma_9_digitos = 0
contador_1 = 10
for digito_1 in cpf_gerado_9_digitos:
    if contador_1 == 1:
        break
    
    digito_X_contador_1 = int(digito_1) * contador_1

    soma_9_digitos += digito_X_contador_1

    contador_1 -=1

'''Multiplicar o resultado anterior por 10'''

soma_9_digitos_X_10 = soma_9_digitos * 10

'''Obter o resto da divisao por 11 da conta anterior'''

resto_11_1 = soma_9_digitos_X_10 % 11

'''Se o resultado anterior > 9 --> 0. Senao --> resultado anterior'''

if resto_11_1 > 9:
    penultimo_digito = 0
else:
    penultimo_digito = resto_11_1

#Gerando o ultimo digito

cpf_gerado_10_digitos = cpf_gerado_9_digitos + str(penultimo_digito)

soma_10_digitos = 0
contador_2 = 11
for digito_2 in cpf_gerado_10_digitos:
    if contador_2 == 1:
        break
    
    digito_X_contador_2 = int(digito_2) * contador_2

    soma_10_digitos += digito_X_contador_2

    contador_2 -=1

'''Multiplicar o resultado anterior por 10'''

soma_10_digitos_X_10 = soma_10_digitos * 10

'''Obter o resto da divisao por 11 da conta anterior'''

resto_11_2 = soma_10_digitos_X_10 % 11

'''Se o resultado anterior > 9 --> 0. Senao --> resultado anterior'''

if resto_11_2 > 9:
    ultimo_digito = 0
else:
    ultimo_digito = resto_11_2

cpf_gerado_final = cpf_gerado_10_digitos + str(ultimo_digito)
print(cpf_gerado_final)