#Metodos de classe --> Sao metodos onde self sera cls, ou seja, ao inves de receber a instancia no primeiro parametro, receberemos a propria classe

'''class BrazilianPerson:
    NATIONALITY = 'Brasileiro' #Atributo de classe
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod #Decorator que transforma o método em método de classe
    def class_method(cls):
        print('Método de classe')

BrazilianPerson.class_method() #Quando um metodo e um metodo de classe, nao precisamos passar uma instancia como argumento'''

#Factories methods --> Podemos usar o classmethod para fazer um factoriemethod --> Factorie method e um metodo que cria instancias de uma classe

class BrazilianPerson:
    NATIONALITY = 'Brasileiro'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def age_bigger_50(cls, name): #Factorie method que cria instancias da classe pessoa somente com idade maior que 50 anos --> E como se fosse uma extensao do molde (classe)
        return cls(name, 50)
    
    @classmethod
    def anonymous(cls, age): #Factorie method
        return cls('Anonimo', age)

p1 = BrazilianPerson.age_bigger_50('Geraldo')
print(p1.name)
print(p1.age)

p2 = BrazilianPerson.anonymous(25)
print(p2.name)
print(p2.age)