#Essa foi uma aula apenas para introduzir os protocolos de collections.abc no Python. Qualquer outro protocolo podera ser implementado seguindo a mesma estrutura usada na aula
#Implementacao do sequence

from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {} #Vamos fazer o dict se comportar como uma lista
        self._index = 0
        self._next_index = 0

    def append(self, *values): #Podemos mudar o comportamento do append para aceitar mais de um elemento de uma vez
        for value in values:
            self._data[self._index] = value
            self._index +=1
    
    def __len__(self): #Temos que definir esse metodo aqui pois na classe Sequence ele e abstrato --> Para ver o tamanho
        return self._index
    
    def __getitem__(self, index): #Temos que definir esse metodo aqui pois na classe Sequence ele e abstrato --> Para usar a notacao 
        return self._data[index]
    
    def __setitem__(self, index, value): #Permite alterar itens da lista com a notacao lista[indice] = valor
        self._data[index] = value
    
    def __iter__(self): #Temos que implementar nosso proprio iterator para evitar erro no for
        return self #Retorna quem sera o iterator. A propria lista sera seu iterator nesse caso
    
    def __next__(self): #Responsavel por retornar o proximo valor de uma lista
        if self._next_index >= self._index: #O self._index recebera o valor do indice do ultimo valor adicionado a lista. Logo, se o self._next_index for maior que esse valor, a iteracao sera interrompida, visto que nao um elemento neste index
            self._next_index = 0 #Precisamos zerar ele para permitir fazermos quantos for quisermos. Ele funciona como um ponteiro, logo, se nao zeramos, um segundo, terceiro ... for seria impossivel
            raise StopIteration #Justamente o que o for faz para parar a iteracao
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value

    
my_list = MyList()
my_list.append('Vitor', 'Nicolas')
my_list.append('Maria')
my_list[0] = 'Joao'
'''print(my_list[0])
print(len(my_list))'''

for item in my_list:
    print(item)

for item in my_list:
    print(item)