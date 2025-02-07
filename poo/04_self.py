#self --> E uma convencao que o primeiro parametro de metodos que retornam coisas diferentes para objetos diferentes deve se chamar self --> O primeiro parametro sempre recebera como argumento a variavel a qual o objeto foi atribuido, independente do nome dele, apesar da convencao ser o self
class Car:
    def __init__(self, model='No model'):
        self.model = model
    
    def accel(self):
        print(f'O carro {self.model} esta acelerando!')

fusca = Car('Fusca')
print(fusca.model)
fusca.accel() # E a mesma coisa que Car.accel(fusca)
'''Car.accel(fusca)'''

celta = Car(model='Celta')
print(celta.model)
celta.accel()