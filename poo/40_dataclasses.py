#O módulo dataclasses fornece um decorador e funcoes para criar metodos como __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
#Em resumo, dataclasses sao sytax sugar para criar classes normais

'''from dataclasses import dataclass'''

'''@dataclass
class Person:
    _name: str
    last_name: str

    def full_name(self): #Podemos definir metodos em dataclasses
        return f'{self.name} {self.last_name}'
    
    @property #Podemos usar getter
    def name(self) -> str:
        return self._name
    
    @name.setter #Podemos usar setter
    def name(self, value: str) -> None:
        self._name = value

p1 = Person('Vitor', 'Silva')
print(p1, p1.__dict__)
print(p1.full_name())
print(p1._name, p1.name)
p1.name = 'Joao'
print(p1._name, p1.name)'''

#__init__ e __post_init___

'''@dataclass#(init=False) #Temos que settar manualmente o __init__ nesse caso. Mesmo definindo o __init__ manualmente, o __post_init__ nao sera executado se init=False
class Person:
    _name: str
    last_name: str

    def __post_init__(self): #Executado apos o __init__
        #print('Após o __init__')
        self.full_name = f'{self._name} {self.last_name}'

p1 = Person('Vitor', 'Silva')
#print(p1.__dict__)

#Configuracoes do decorator dataclasse

@dataclass#(eq=True, frozen=True, order=True)
#eq=False --> Destativa __eq__
#frozen=True --> Nao podemos setar nenhum atributo alem daqueles definifos no inicio --> Boa pratica de programacao
#order=True --> Ordena uma variavel composta que recebe objetos da classe --> eq deve ser True --> Ordena pela ordem dos atributos passados na criacao da dataclass
class Person:
    _name: str
    last_name: str

#p1 = Person('Vitor', 'Lima')
#p1._name = 'Joao' #Da um erro pois a classe esta com frozen=True
person_list = [Person('C', 'Y'), Person('A', 'Z'), Person('B', 'X'),]
#order_person_list = sorted(person_list)

##Podemos criar nosso proprio ordenamento
order_person_list = sorted(person_list, key=lambda person: person._name)
print(order_person_list)'''

#asdict e astuple
##Converte o objeto da nossa classe em dict ou tuple

'''from dataclasses import dataclass, asdict, astuple

@dataclass
class Person:
    _name: str
    last_name: str

p1 = Person('Vitor', 'Silva')
p1_dict = asdict(p1)
p1_tuple = astuple(p1)

print(p1.__dict__)#So pra ver que e igual ao dict gerado pela dataclass
print(p1_dict) #Podemos usar todos os metodos de dict
print(p1_tuple) #Podemos usar todos os metodos de tuple'''

#Valores padrão, field e fields em dataclasses

from dataclasses import dataclass, asdict, field

@dataclass
class Person:
    _name: str = 'Missing value'
    last_name: str = field(default='Missing value')
    age: int = 0 #Podemos atribuir apenas valores imutaveis como padrao
    adresses: list[str] = field(default_factory=list) #Temos que usar esse artificio para settar valor mutavel como padrao

print(asdict(Person('Vitor', 'Silva',)))
print(asdict(Person(age=24, adresses=['Minha casa'])))