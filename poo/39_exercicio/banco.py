from random import randint
from faker import Faker
from funcoes_autenticacao import ag_auth, client_auth, acc_auth

class Bank:
    def __init__(self) -> None:
        self.name = f'{Faker().name()} Bank'

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'

    def set_ags(self) -> None:
        self.ags = []

        for number in range(0, 3):
            if number == 0:
                ag = randint(0, 3)
                self.ags.append(ag)
            else:
                while self.ags.count(ag):
                    ag = randint(0, 3)
                self.ags.append(ag)

    def set_acc_numbers(self) -> None:
        self.acc_numbers = []

        for number in range(0, 3):
            if number == 0:
                acc_number = randint(0, 3)
                self.acc_numbers.append(acc_number)
            else:
                while self.acc_numbers.count(acc_number):
                    acc_number = randint(0, 3)
                self.acc_numbers.append(acc_number)
    
    def set_clients(self) -> None:
        self.clients = ['Vitor Lima', Faker().name(), Faker().name()]

        #for number in range(0, 3):
        #    self.clients.append(Faker().name())
    
    def auth_method(self: object, client: object) -> None:
        client_auth_ = client_auth(self, client)
        if not client_auth_:
            print('Cliente não encontrado. Encerrando operação...')
            return
        
        ag_auth_ = ag_auth(self, client)
        if not ag_auth_:
            print('Agência não encontrada. Encerrando operação...')
            return
        
        acc_auth_ = acc_auth(self, client)
        if not acc_auth_:
            print('Conta não encontrada. Encerrando operação...')
            return

        if ag_auth_ and client_auth_ and acc_auth_:
            client.acc_.withdraw()

if __name__ == '__main__': #Executar testes so aqui
    random_bank = Bank()
    random_bank.set_ags()
    random_bank.set_acc_numbers()
    random_bank.set_clients()
    print(random_bank.__dict__)