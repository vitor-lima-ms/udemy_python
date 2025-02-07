#Metodos estaticos sao metodos que estao dentro da classe, mas nao tem acesso ao self nem ao cls --> Sao funcoes que existem dentro da classe

class Class:
    @staticmethod
    def function(): #Metodos estatico
        print('Eu sou inutil')
    
c1 = Class()
c1.function() #Podemos acessa-la pela instancia
Class.function() #Ou pela classe

#E a mesma coisa que definir uma funcao fora da classe --> Mas ela nao estara protegida pelo prefixo da classe