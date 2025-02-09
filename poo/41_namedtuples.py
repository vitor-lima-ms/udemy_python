#Tuplas (imutaveis como ja vimos) com nomes para valores
#Muito usada para criar classes de objetos que sao apenas um agrupamento de atributos, como classes normais sem metodos, ou registros de base de dados, linhas de arquivos csv

'''from collections import namedtuple

Card = namedtuple('Card', ['Valor', 'Naipe'], defaults=['Valor padrão', 'Naipe padrão']) #Criando uma classe

ace_spades = Card('A', 'Espadas')
print(ace_spades)
print(ace_spades.Valor) #Podemos acessar assim ao inves de utilizar indice
print(ace_spades[0])
print(ace_spades.Naipe)
print(ace_spades[1])

for value in ace_spades:
    #print(value)
    #print(ace_spades._fields) #Acesso aos fieds
    #print(ace_spades._field_defaults) #Acesso aos valores default
    print(ace_spades._asdict()) #Retorna um dicionario'''

#Podemos criar uma classe de namedtuple herdando tambem

from typing import NamedTuple

class Card(NamedTuple): #Prof prefere essa
    Valor: str = 'Valor padrão'
    Naipe: str = 'Naipe padrão'

ace_spades = Card('A', 'Espadas')

for value in ace_spades: #Mesmas funcionalidades de cima
    print(value)
    print(ace_spades._fields)
    print(ace_spades._field_defaults)
    print(ace_spades._asdict())