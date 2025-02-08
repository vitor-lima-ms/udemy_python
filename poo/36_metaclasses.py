#Metaclasses sao o tipo das classes
#Em Python, tudo e um objeto, inclusive as classes
    #Seu objeto e uma instancia da sua classe
    #Sua classe e uma instancia de type (type e uma metaclasse)
#Ao criar uma classe, coisas ocorrem por padrao, nessa ordem
    #__new__ da metaclasse e chamado e cria a nova classe
    #__call__ da metaclasse e chamado com os argumentos e chama:
        #__new__ da classe com os argumentos (cria a instancia)
        #__init__ da classe com os argumentos
    #__call__ da metaclass termina a execucao
#Metodos importantes da metaclasse
    #__new__(mcs, name, bases, dct) (Cria a classe)
    #__call__(cls, *args, **kwargs) (Cria e inicializa a instancia)

Foo = type('Foo', (object,), {}) #type cria classes --> args: nome da classe, de quem ela herda (por padrao e da object) e o dicionario da classe

f = Foo()
print(type(f))