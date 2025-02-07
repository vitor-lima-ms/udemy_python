'''Criar as classes Carro (com nome), Motor (com nome) e Fabricante (com nome). Fazer a ligacao entre Carro e Motor (Um motor pode ser de varios carros). Fazer a ligacao entre Carro e Fabricante (Um fabricante pode fabricar varios carros)
'''

class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

class Engine:
    def __init__(self, name):
        self.name = name

class Manufacturer:
    def __init__(self, name):
        self.name = name

car = Car('Up!')
engine = Engine('1.0')
manufacturer = Manufacturer('Volkswagen')

car.engine = engine
car.manufacturer = manufacturer

print(f'O nome do carro e {car.name}, tem um motor {car.engine.name} e foi fabricado pela {car.manufacturer.name}.')