#Para criar uma exception em Python, so precisamos herdar de alguma excecao da linguagem
    #A recomendacao da documentacao e herdar da classe Exceptions

#Criando excecoes (a convencao e colocar Error ao final da classe que estamos criando)
class MyError(Exception): #So isso aqui ja cria uma excecao nossa
    ...

class OtherError(Exception):
    ...

#Levantando (raise)/Lancando (throw) um excecao
def throw():
    excpt = MyError('Mensagem do meu erro.')
    excpt.add_note('Notas de erro')
    raise  excpt

#throw()

#Tratando mais de um erro
try:
    throw()
except (MyError, ZeroDivisionError) as error: #Podemos tratar mais de um erro
    print(error.__class__.__name__) #Exibe qual o nome da classe do erro que foi gerado
    print(error) #Mostra so a 'Mensagem do meu erro.'
    '''raise #Relancando a excecao como ela veio'''
    raise OtherError('Relancando') from error #Relancando outro erro criado por mim