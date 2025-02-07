#__init__
class Person: #__init__ sempre retorna None
    def __init__(self, name, last_name): #Um dos primeiros metodos a ser executado em toda a classe --> O parametro self ira receber a variavel que esta recebendo a instancia da classe --> Utilizado para atribuir atributos diferentes aos objetos criados a partir da classe --> Ex: Cada pessoa (objeto) tera nome e sobrenome (atributos) diferentes
        self.name = name
        self.last_name = last_name  

#Criando um objeto a partir da classe Person
person00 = Person('Vitor', 'Lima') 
'''print(person00)''' #--> <__main__.Person object at 0x7f89013fab10>
print(person00.name)
print(person00.last_name)

person01 = Person('Maria', 'Clara') #Um segundo objeto da classe Person
print(person01.name)
print(person01.last_name)