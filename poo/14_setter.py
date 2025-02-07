#Property pode ser utilizada:
    #P/ habilitar setter --> Metodo utilizado para configurar determinado atributo
    #P/ utilizar @setter, precisamos do @property

class Pen:
    def __init__(self, color):
        print('Nao passei no setter.')
        self._color = color #_ ou __ antes do atributo e para comunicar que esse atributo nao deve ser utilizado fora da classe --> ELe e somente um artifico para armazenar um valor
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if value == 'rosa': #Dentro do setter podemos controlar os valores que serao aceitos
            raise ValueError('Cor nao permitida!')

        print('Passei no setter.')
        self._color = value
        
bic = Pen('azul')
print(bic.color)

bic.color = 'vermelho'
print(bic.color)