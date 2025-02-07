#E um getter no modo Pythonico
    #Getter --> Um metodo para obter um atributo
#property --> E uma propriedade do objeto --> Um metodo que se comporta como um atributo
#Usada nas seguintes situacoes:
    #Como getter --> Funcao que retorna uma atributo de um objeto --> Protege o atributo (e.g., podemos mudar o nome dele de boa, pois so teremos que alterar na funcao get)
    #P/ evitar quebrar o codigo cliente --> E o codigo que usa seu codigo
    #P/ habilitar setter
    #P/ executar acoes ao obter um atributo --> Codigo no escopo da funcao get (antes do return)

class Pen:
    def __init__(self, color):
        self.new_color = color

    def get_color(self): #Modo tradicional do getter
        return self.color

    @property
    def color(self):
        return self.new_color

bic = Pen('azul')
'''print(bic.get_color())'''

print(bic.color) #Mesmo que o atributo seja new_color, consigo utilzar o color pois defini um property com o nome color que retorna o new_color