#Gera numeros aleatorios seguros

import secrets

#print(secrets.randbelow(100)) #Gera um numero aleatorio abaixo de 99

#secrets.choice(lista) --> Escolhe aleatoriamente um elemento de uma lista

random = secrets.SystemRandom() #Permite que a gente utilize as funcionalidades do random

#Criando uma senha

import string as s
from secrets import SystemRandom as Sr

'''print(s.ascii_letters) #String com todas as letras (tanto maiusc quanto minusc)
print(s.digits) #Numeros
print(s.punctuation) #Pontuacoes'''

password = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=20)) #Concateno todas as letras, numeros e pontuacoes --> Utilizo o choices pra escolher quantos caracteres eu quiser --> Utilizo o join em uma string vazia para criar uma senha
print(password)