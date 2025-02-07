#Modificadores de acesso --> public, protected e private
#O Python nao tem modificadores de acesso, mas podemos seguir as seguintes convencoes:
    #sem _ --> public --> Pode ser usado em qualquer lugar
    #_ --> protected --> Nao deve ser usado fora da classe ou suas subclasses
    #__ --> private --> So deve ser usado na classe em que foi declarado
        #Isso e conhecido como naming mangling (desfiguracao de nome)

class Random:
    def __init__(self):
        self.public = 'Isso e public.'
        self._protected = 'Isso e protected.'
        self.__private = 'Isso e private'

    def public_method(self):
        print(self._protected) #Aqui dentro posso usar os protecteds
        print(self._protected_method()) #Aqui dentro posso usar os protecteds
        
        print(self.__private) #Aqui dentro posso usar os privates, mas em subclasses nao
        print(self.__private_method()) #Aqui dentro posso usar os privates, mas em subclasses nao

        return ('Metodo public.')
    
    def _protected_method(self):
        return ('Metodo protected.')
    
    def __private_method(self):
        return ('Metodo private.')

a = Random()

print(a.public)
print(a.public_method())

'''print(a._protected) #Nao deveria poder fazer isso --> Mas e uma convencao, a linguagem nao tem um mecanismo para impedir isso
print(a._protected_method())'''