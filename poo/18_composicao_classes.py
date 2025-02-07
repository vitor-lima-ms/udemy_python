#E uma especializacao da agregacao
    #Mas nela, quando o objeto 'pai' for apagado, todas as referencias dos objetos filhos tambem sao apagadas
#E DONO DE UM OBJETO

class Client:
    def __init__(self, name):
        self.name = name
        self.adress = []

    def insert_adress(self, street, number):
        self.adress.append(Adress(street, number)) #Os enderecos devem ser criados dentro da classe Client --> A instancia do Adress esta sendo criada dentro da classe Client --> Quando uma instancia da classe Client deixar de existir, a instancia da classe Adress associada a ela tambem deixara de existir

    def list_adress(self):
        for adress in self.adress:
            print(adress.street, adress.number)
    
    def __del__(self):
        print('Apagando', self.name)

class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number
    
    def __del__(self):
        print('Apagando', self.street, self.number)

client00 = Client('Vitor')
client00.insert_adress('Luiz Orsini', 200)

'''print(client00.adress[0].street) #Acessando o objeto dentro da lista
print(client00.adress[0].number) #Acessando o objeto dentro da lista'''

client00.list_adress() #Outra forma de acessar

'''del client00''' #Se eu deletar o cliente antes, o garbage colector inicia antes do final do codigo

print('Acabou o código') #O metodo __del__ apaga as instancias apos a finalizacao do codigo --> Garbage colector