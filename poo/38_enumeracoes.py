#Enumeracoes na programacao sao usadas em ocasioes onde temos um determinado numero de coisas para escolher
#Enums tem membros e seus valores sao constantes
#Enums em Python:
    #Sao um conjunto de nomes simbolicos (podemos pensar como chaves) ligados a valores unicos
    #Podem ser iterados para retornar seus membros canonicos na ordem de definicao
#enum.Enum e a superclasse para as enumeracoes. Mas tambem pode ser usada diretamente (mesmo assim, Enums nao sao classes normais em Python)
#Podemosusar um Enum com type annotations, com isinstance e outras coisas relacionadas com tipo
#Para obter os dados:
    #membro = Classe(valor), Classe['chave']
    #chave = Classe.chave.name
    #valor = Classe.chave.value --> Enumeracao em si --> Comeca do 1
import enum

'''Directions = enum.Enum('Direções', ['ESQUERDA', 'DIREITA'])
print(Directions(1).name, Directions['ESQUERDA'].value)

def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direção não encontrada.')

    print(f'Movendo para {direction.name}.')

move(Directions.ESQUERDA)
move(Directions.DIREITA)
move('Lado')'''

#Se o editor de texto nao reconhecer a classe direito --> Fazer o que esta abaixo

class Directions(enum.Enum):
    ESQUERDA = 1 #Podemos utilizar enum.auto()
    DIREITA = 2

print(Directions(1).name)
print(Directions(2).name)