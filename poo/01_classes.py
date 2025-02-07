#Classes sao moldes para criar novos objetos
#As classes geram novos objetos (instancias) que podem ter seus proprios atributos e metodos
    #Atributos --> Dados dentro da classe
    #Metodos --> Acoes/funcoes dentro da classe
#Os objetos gerados pela classe podem usar seus dados internos para realizar varias acoes
#Por convecao, usamos PascalCase (toda palavra comeca com letra maiuscula) para nomes de classes

string = 'Vitor' #Instancia da classe str --> Atributo nesse caso seriam as letras da string
#Ja usamos muitos metodos da classe str em instancias dessa clase (.upper(), .lower() etc.)
'''print(isinstance(string, str))''' #--> True
#str e uma classe padrao do Python

#Para criar uma classe
class Person:
    ...#Aqui vem os atributos e metodos da classe


#Criando um objeto a partir da classe Person
person00 = Person() #Precisamos utilizar o parenteses para criar a instancia dessa classe
'''print(person00)''' #--> <__main__.Person object at 0x7f89013fab10>
person00.name = 'Vitor'
person00.last_name = 'Lima' #Para acessar atributos --> Sempre sem parenteses
print(person00.name)
print(person00.last_name)

person01 = Person() #Um segundo objeto da classe Person
person01.name = 'Maria'
person01.last_name = 'Clara'
print(person01.name)
print(person01.last_name)