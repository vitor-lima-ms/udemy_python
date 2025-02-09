from random import randint
from faker import Faker
from funcoes_autenticacao import ag_auth, client_auth, acc_auth

class Bank:
    def __init__(self):
        self.name = f'{Faker().name()} Bank'

    def __repr__(self):
        class_name = self.__class__.__name__
        inst_dict = self.__dict__
        return f'{inst_dict} ({class_name})'

    def set_ags(self):
        self.ags = []

        for number in range(0, 3):
            self.ags.append(randint(0, 3))

    def set_acc_numbers(self):
        self.acc_numbers = []

        for number in range(0, 3):
            self.acc_numbers.append(randint(0, 3))
    
    def set_clients(self):
        self.clients = ['Vitor Lima']

        #for number in range(0, 3):
        #    self.clients.append(Faker().name())
    
    def auth_method(self, client):
        ag_auth_ = ag_auth(self, client)
        if not ag_auth_:
            print('Agência não encontrada. Encerrando operação...')
            return

        client_auth_ = client_auth(self, client)
        if not client_auth_:
            print('Cliente não encontrado. Encerrando operação...')
            return
        
        acc_auth_ = acc_auth(self, client)
        if not acc_auth_:
            print('Conta não encontrada. Encerrando operação...')

        if ag_auth_ and client_auth_ and acc_auth_:
            client.acc_.withdraw()

if __name__ == '__main__': #Executar testes so aqui
    random_bank = Bank()
    random_bank.set_ags()
    random_bank.set_acc_numbers()
    random_bank.set_clients()
    print(random_bank.__dict__)