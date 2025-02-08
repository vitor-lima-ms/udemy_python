'''class MyString (str): #Herdou todos os metodos da classe str
    def upper(self):
        print('Meu .upper()')
        result = super().upper() #Poderia fazer dessa forma tb caso quisesse realizar alguma acao depois de retornar o metodo da superclasse
        return super().upper() #Permite que eu define alguma coisa no escopo do meu metodo sem inutilizar o metodo da superclasse

my_string = MyString('Vitor')
print(my_string.upper()) #Se eu definir um metodo upper na MyString, vou estragar o metodo upper da classe str --> MRO comeca na classe filha --> Contudo, podemos usar a classe super() dentro do metodo para que o metodo da superclasse seja utilizado'''

class A:
    attr_a = 'A attr'
    def method(self):
        print('A')

class B(A):
    attr_b = 'B attr'
    def method(self):
        print('B')

class C(B):
    attr_c = 'C attr'
    def method(self):
        super(C, self).method() #A partir dessa classe, procure outra classe com o metodo method que, nesse caso, e B. Poderiamos passar B como argumento, entao o metodo seria buscado em A
        print('C')

c = C()
print(c.attr_a)
print(c.attr_b)
print(c.attr_c) #C herdou tudo de B que herdou de A. Apenas o metodo que nao, pois ele tem o mesmo nome nas 3, logo o MRO so utilizara o de C
print(C.mro()) #Metodo de classe que retorna o MRO