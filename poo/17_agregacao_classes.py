#E uma forma mais especializada de associacao entre dois ou mais objetos
#Cada objeto tera ser ciclo de vida independente --> Se um objeto for apagado, o outro continua existindo e vice-versa
#Geralmente e uma relacao de um para muitos, onde um objeto tem um ou muitos objetos
#Os objetos podem viver separadamente, mas pode se tratar de uma relacao onde um objeto precisa de outro para fazer determinada tarefa --> Pensar em carro e roda --> Ambos existem separadamente mas o carro nao funciona perfeitamente sem a roda
    #Existem controversias sobre as definicoes de agregacao
#UM OBJETO TEM OUTRO OBJETO
class ShopingChart:
    def __init__(self):
        self._products = [] #Nao precisa ser acessado fora da classe
    
    def insert_products(self, *products):
        for product in products:
            self._products.append(product)
    
    def list_products(self):
        for product in self._products:
            print(product.name, product.price) #Os atributos aqui tem que ter os mesmos nomes dos atributos dos objetos da classe Product
    
    def total_price(self):
        return sum([
            product.price for product in self._products #Os atributos aqui tem que ter os mesmos nomes dos atributos dos objetos da classe Product
        ])

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

shop_chart = ShopingChart()
p1, p2 = Product('Caneta', 1.20), Product('Blusa', 20.00)

shop_chart.insert_products(p1, p2)
shop_chart.list_products()

total_price = shop_chart.total_price()
print(total_price)

'''Isso e uma agregacao pois os objetos da classe ShoppingChart agregam objetos da classe Product'''