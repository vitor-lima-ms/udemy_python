#Familia de classes que vai utilizar os mixins

from log import LogPrintMixin, LogFileMixin
from time import sleep

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._online = False
    
    def turn_on(self):
        if not self._online:
            print(f'Ligando {self._name}...')
            self._online = True
            sleep(2)
            print(f'{self._name} ligado.')
            return
        
        print('O dispositivo já está ligado.')

    def turn_off(self):
        if self._online:
            print(f'Desligando {self._name}...')
            self._online = False
            sleep(2)
            print(f'{self._name} desligado.')
            return
        
        print('O dispositivo já está ligado.')

class Smartphone(Eletronic):
    def turn_on(self): #Definimos os metodos da classe mae aqui apenas para utilizar os mixins
        super().turn_on() #Repassando a execucao para a superclasse Eletronic. Se eu quisesse fazer alguma coisa antes ou depois de passar para a classe super, deveria jogar esse resultado em uma variavel e retorna-la

        #Forma com heranca multipla

        '''if self._online:
            log_print = LogPrintMixin()
            log_print.log_success(f'{self._name} ligado.')

            log_file = LogFileMixin()
            log_file.log_success(f'{self._name} ligado.')''' #Forma que eu consegui fazer sozinho
    
    def turn_off(self):
        super().turn_off()