class Person:
    CURRENT_YEAR = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birth_year(self):
        return Person.CURRENT_YEAR - self.age
    
'''p1 = Person('Vitor', 25)
print(p1.__dict__)''' #Dicionario que guarda os atributos das instancias --> Nao e so leitura --> Podemos manipular diretamente com .__dict__[nova_chave]: valor
'''print(vars(p1))''' #Tambem mostra do dicionario

p1_data = {'name': 'Vitor', 'age': 25} #Podemos criar um objeto a partir do dicionario
p1 = Person(**p1_data) #Temos que desempacotar
print(p1.name)
print(p1.age)
print(vars(p1))