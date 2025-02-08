def repr_add(cls): #Funcao para adicionar o repr a classe
    def my_repr(self):
        class_name = self.__class__.__name__
        instance_dict = self.__dict__
        instance_repr = f'{class_name} ({instance_dict})'
        return instance_repr
    cls.__repr__ = my_repr #Nao preciso executar a funcao aqui pois o self sera passado automaticamente quando eu chamar o objeto
    return cls

@repr_add #Preciso decorar as classes com o repr_add
class SoccerTeam:
    def __init__(self, name):
        self.name = name

@repr_add
class Planet:
    def __init__(self, name):
        self.name = name

brazil = SoccerTeam('Brasil')
portugal = SoccerTeam('Portugal')
earth = Planet('Terra')
mars = Planet('Marte')

print(brazil)
print(earth)