#Metodos --> Metodos de instancia --> self --> Acesso as instancias
#Metodos de classe --> cls --> Acesso a classe
#Metodos estaticos --> Nao acessa instancias nem classe

class Connection:
    def __init__(self, host='localhost', user=None, password=None): #Metodo de instancia
        self.host = host
        self.user = user
        self.password = password

    def set_user(self, user): #Setter
        self.user = user
    
    def set_password(self, password):
        self.password = password
    
    @classmethod
    def std_connection(cls):
        return cls(user='admin', password='123')
    
    @staticmethod
    def log(string):
        return string

user00 = Connection()
user00.set_user('Vitor')
user00.set_password('170500')
print(user00.user, user00.password)

std_user = Connection.std_connection()
print(std_user.user, std_user.password)

log = Connection.log('Mensagem do log')
print(log)