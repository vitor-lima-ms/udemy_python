#callable e algo que pode ser executado com parenteses
#Em classes normais, __call__ faz a instancia de uma classe ser callable

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(f'{name} está ligando para {self.phone}')

call = CallMe('(31) 9 9837-1486')
call('Simone') #Posso chamar o objeto com () diretamente