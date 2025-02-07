#Metodo --> Funcao que esta dentro da classe --> Sempre que ela for retornar coisas diferentes para objetos diferentes, temos que usar o self
class Car:
    def __init__(self, model='No model'):
        self.model = model
    
    def accel(self):
        print(f'O carro {self.model} esta acelerando!')

fusca = Car('Fusca')
print(fusca.model)
fusca.accel()

celta = Car(model='Celta') #Podemos passar como kwargs
print(celta.model)
celta.accel()