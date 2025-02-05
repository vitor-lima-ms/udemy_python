'''Criar funcoes que duplicam, triplicam e quadruplicam um numero recebido'''

def coletora_numero(num):
    def duplicar(mult=2):
        return num * mult
    def triplicar(mult=3):
        return num * mult
    def quadruplicar(mult=4):
        return num * mult
    return  duplicar, triplicar, quadruplicar

numero_inteiro = int(input('Digite um numero inteiro: '))
tupla_funcoes_d_t_q = coletora_numero(numero_inteiro) #Isso aqui gera uma tupla com as funcoes duplicar, triplicar e duplicar para o numero que o usuario passar

lista_resultados = []
for funcao in tupla_funcoes_d_t_q: #Posso acessar cada funcao da tupla e utilizar os parenteses para retornar o valor do return, que no caso sera o numero digitado pelo usuario * 2, * 3 e * 4
    lista_resultados.append(funcao())

contador = 2
for resultado in lista_resultados:
    print(f'O resultado da multiplicação por {contador} é {resultado}')
    contador += 1