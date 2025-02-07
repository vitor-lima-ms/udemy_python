'''Criar funcoes que duplicam, triplicam e quadruplicam um numero recebido'''

def coletora_numero(num):
    def multiplicadora(multiplicador):
        return num * multiplicador
    return multiplicadora

numero_inteiro = int(input('Digite um numero inteiro: '))
funcao_multiplicadora = coletora_numero(numero_inteiro)

multiplicador = int(input('Digite o multiplicador: '))
resultado = funcao_multiplicadora(multiplicador)

print(f'O resultado da multiplicação entre {numero_inteiro} e {multiplicador} é {resultado}')