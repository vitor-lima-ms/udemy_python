from abc import ABC, abstractmethod
from contas import CheckingAcc, SavingsAcc
from random import randint

class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: int) -> None:
        self._name = value

    @property
    def age(self) -> str:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        self._age = value    

class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def acc(self) -> None:
        acc_type = input('Tipo da conta [Corrente ou Poupança]: ')

        while acc_type.lower() not in 'corrente' and acc_type.lower() not in 'poupança':
            print('Opção inválida!')
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