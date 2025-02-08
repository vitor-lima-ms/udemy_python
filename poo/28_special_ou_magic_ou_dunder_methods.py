#Dunder --> Double Underscore --> Coisas que ja existem na linguagem
    #__lt__(self, other) --> self < other
    #__le__(self, other) --> self <= other
    #__gt__(self, other) --> self > other
    #__ge__(self, other) --> self >= other
    #__eq__(self, other) --> self == other
    #__ne__(self, other) --> self != other
    #__add__(self, other) --> self + other
    #__sub__(self, other) --> self - other
    #__mul__(self, other) --> self * other
    #__truediv__(self, other) --> self / other
    #__neg__(self) --> -self
    #__str__(self) --> str (chamar a string do metodo)
    #__repr__(self) --> str
    #Existem muitos outros
    #https://rszalski.github.io/magicmethods/

#__repr__ --> Comunica com outros desenvolvedores como um objeto seria remontado em Python
'''class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self): #Mais informal --> Se nao definirmos o fallback e o __repr__
        return f'{self.x}, {self.y}'

    def __repr__(self): #Tem que retornar uma string
        class_name = type(self).__name__ #Ou class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'#Usar o !r aqui para comunicar melhor     

p1 = Coordinate(1, 2)
p2 = Coordinate(3, 4)

print(p1)
print(repr(p2)) #Funcao para ver o __repr__
print(f'{p2!r}') #Outra forma de ver o __repr__ --> !s retorna o __str__'''

#Exemplos de aplicacao de outros dunder methods

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self): #Tem que retornar uma string
        class_name = type(self).__name__ #Ou class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'#Usar o !r aqui para comunicar melhor

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinate(new_x, new_y) #Preciso retornar a criacao do objeto
    
    def __gt__(self, other):
        self_result = self.x + self.y
        other_result = other.x + other.y
        if self_result > other_result:
            return True
        return False

if __name__ == '__main__':
    p1 = Coordinate(4, 2)
    p2 = Coordinate(6, 4)
    p3 = p1 + p2
    print(p3)
    print('p1 é maior do que p2:', p1 > p2)
    print('p2 é maior do que p1:', p2 > p1)