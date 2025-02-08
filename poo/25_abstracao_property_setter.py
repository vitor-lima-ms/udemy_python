from abc import ABC, abstractmethod

class AbstractFoo(ABC): #Foo e Bar sao palavras usadas como placeholder --> Palavras que podem mudar na programacao
    def __init__(self, name):
        self._name = name
    
    @property
    @abstractmethod
    def name(self):
        ...

    '''@name.setter
    def name(self, value):
        self._name = value''' #Nao preciso do setter aqui

class Foo(AbstractFoo):
    '''name = ""''' #Poderiamos fazer isso aqui ao inves de criar o conjunto @property @setter
    
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

foo = Foo('Bar')
print(foo.name)