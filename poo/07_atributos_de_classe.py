'''CURRENT_YEAR = 2025''' #Evitar hard coded --> Variaveis constantes sempre com todas as letras maiusculas

class Person:
    CURRENT_YEAR = 2025 #Atributo da classe --> Todas as instancias vao utilizar esse valor --> Podemos acessa-lo com o self. em cada instancia --> Melhor usar o nome da classe

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birth_year(self):
        return Person.CURRENT_YEAR - self.age
    
p1 = Person('Vitor', 25)
p2 = Person('Maria', 23)

print(f'O ano atual e {Person.CURRENT_YEAR}')

'''Person.CURRENT_YEAR = ...''' #Se eu mudar aqui, altera em todas as instancias e, consequentemente, altero a conta do ano

print(p1.birth_year())
print(p2.birth_year())