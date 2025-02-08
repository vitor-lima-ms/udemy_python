def method_decorator(method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'Você está em casa'
        return result
    
    return inner

class Planet:
    def __init__(self, name):
        self.name = name

    @method_decorator
    def show_name(self):
        return f'O nome do planeta é {self.name}'

earth = Planet('Terra')
mars = Planet('Marte')

print(earth.show_name())
print(mars.show_name())