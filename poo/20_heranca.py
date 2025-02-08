#Heranca simples --> Relacao entre classes

#Classe principal (e.g., Pessoa) --> super class, base class, parent class
    #Classes filhas (e.g., Cliente) --> sub class, child class, derived class
    #A classe Pessoa pode ser enxergada como uma generalizacao da classe Cliente --> Cliente e uma Pessoa
    #Poderiamos ter feito o processo contrario e especializado Pessoa em Cliente --> Especializacao
#Em Python, todas as classe ja herdam de um builtin --> Coisas que ja vem por padrao no Python

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def speak_class_name(self):
        print(self.name, self.last_name, self.__class__.__name__) #Exibir o nome da classe que esta chamando o metodo

class Client(Person): #Client herda de Person. Todo codigo que esta dentro de Person e automaticamente usado por Client
    ...

class Student(Person):
    ...

c1 = Client('Vitor', 'Silva')
s1 = Student('Maria', 'Silva')

c1.speak_class_name() # --> class Client
s1.speak_class_name() # --> class Student

#Method resolution order (MRO) --> Ordem que o Python para procurar metodos e atributos --> Usar help(Classe) para ver a MRO