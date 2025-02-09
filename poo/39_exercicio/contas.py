from abc import ABC, abstractmethod

class Acc(ABC):

    def __init__(self, ag: int, acc_number: int, balance: int) -> None:
        self.ag = ag
        self.acc_number = acc_number
        self._balance = balance
        print(f'Balanço: R${self._balance}')
    
    @abstractmethod
    def withdraw(self) -> None:
        value = float(input('Valor do saque: R$'))
        self._balance -= value

        if self._balance < self._LIMIT:
            print(f'Saque negado. O saldo R${self._balance} ficará menor que o limite.')
            self._balance += value
        else:
            print(f'Saque de R${value} autorizado. Novo saldo: R${self._balance}')
            self._balance -= value
    
    def deposit(self) -> None:
        value = float(input('Valor do depósito: R$'))
        self._balance += value
        print(f'Novo saldo: R${self._balance}')

class CheckingAcc(Acc):
    _LIMIT = -200

    def __init__(self, ag, acc_number, balance):
        super().__init__(ag, acc_number, balance)
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'
    
    def withdraw(self):
        super().withdraw()

class SavingsAcc(Acc):
    _LIMIT = 0

    def __init__(self, ag, acc_number, balance):
        super().__init__(ag, acc_number, balance)
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'
    
    def withdraw(self):
        super().withdraw()
    
if __name__ == '__main__': #Executar testes so aqui
    c1 = CheckingAcc(1, 2, 1000)
    print(c1)
    c2 = SavingsAcc(3, 4, 2000)
    print(c2._LIMIT)

    '''c2.withdraw()
    c2.deposit()'''

    '''c1.withdraw()
    c2.withdraw()'''