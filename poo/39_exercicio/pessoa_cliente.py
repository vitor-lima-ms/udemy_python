from abc import ABC, abstractmethod
from contas import CheckingAcc, SavingsAcc
from random import randint

class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    def __repr__(self):
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: int):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value: int):
        self._age = value    

class Client(Person):
    def __init__(self, name, age: int):
        super().__init__(name, age: int)
    
    def acc(self):
        acc_type = input('Tipo da conta [Corrente ou Poupança]: ')
        
        if acc_type in 'Corrente':
            self.acc_ = CheckingAcc(randint(0, 3), randint(0,3), randint(0, 9999))
            
        elif acc_type in 'Poupança':
            self.acc_ = SavingsAcc(randint(0, 3), randint(0,3), randint(0, 9999))

if __name__ == '__main__': #Executar testes so aqui
    p1 = Client('Vitor', 24)
    
    '''p1.acc()
    p1.acc_.deposit()
    p1.acc_.withdraw()

    print(p1.acc_.__dict__)'''
    print(p1.__dict__)