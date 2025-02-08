class Animal:
    '''name = Lion''' #A classe pode ter seu proprio escopo --> Atributos de classe

    def __init__(self, name):
        self.name = name

        var = 'Variavel do escopo do __init__'
        print(var) #Sera executado sempre que eu chamar um atributo

    def eating(self, food):
        return f'{self.name} esta comendo {food}'
    
    def do(self, *args, **kwargs):
        return self.eating(*args, **kwargs) #Funcao que retorna a execucao de outra

lion = Animal('Leao')
print(lion.name)
print(lion.eating('carne'))
print(lion.do(('carne', 'zebra')))