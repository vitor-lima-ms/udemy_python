#No Python, uma classe pode estender varias outras classes
#Heranca simples
    #Animal --> Mamifero --> Humano --> Pessoa --> Cliente
#Heranca multipla e mixins --> Mixin e uma classe (Log nesse caso) que nao faz parte da familia (Cliente, Pessoa, Humano...)
    #Log --> FileLog
    #Animal --> Mamifero --> Humano --> Pessoa --> Cliente
    #Cliente(Pessoa, FileLog)
#O Python usa o C3 superclass linearization para gerar o MRO
#Para saber a ordem de chamada dos metodos --> Usar o metodo de classe .mro() ou o atributo __mro__
#Probelma do diamante
class A:
    ...
    def whoim(self):
        print('A')

class B(A):
    ...
    '''def whoim(self):
        print('B')'''

class C(A):
    ...
    def whoim(self):
        print('C')

class D(B, C): #Essa ordem importa --> Altera o C3 --> A classe que vem primeiro entre parenteses tem grandes chances de ser a escolhida
    ...
    '''def whoim(self):
        print('D')'''

d = D()
d.whoim()
print(D.mro())