from pessoa_cliente import Client
from banco import Bank
from time import sleep

#Criando o cliente
c = Client('Vitor Lima', 24)
print('CLIENTE')
print(c.__dict__)
print()

#Criando a conta do client
sleep(3)
print('CONTA DO CLIENTE')
c.acc()
print(c.acc_.__dict__)
print()

#Criando o banco
sleep(3)
b = Bank()
b.set_ags()
b.set_acc_numbers()
b.set_clients()
print('BANCO')
print(b.__dict__)
print()

#Autenticacao
sleep(3)
b.auth_method(c)