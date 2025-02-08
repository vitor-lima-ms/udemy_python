#Sao construtores --> Metodos que criam objetos
#__new__ e o metodo responsavel por criar e retornar um novo objeto --> Por isso, recebe cls
#__init__ e o metodo responsavel por inicializar uma instancia --> Por isso, recebe self
    #Muito mais utilizado que o __new__
    #Deve retornar None --> Ou seja, nao deve retornar nada
#object e a superclasse de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        print('Posso fazer coisas antes da criação do objeto.')
        instance = super().__new__(cls)
        print('Posso fazer coisas depois da criação do objeto.')
        return instance
    
    def __init__(self):
        print('Sou o __init__.')

a = A()