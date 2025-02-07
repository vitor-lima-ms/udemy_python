class Camera:
    def __init__(self, name, filming=False):
        self.name = name #Os atributos sempre ficam salvos e o escopo dos metodos podem mudar esses atributos
        self.filming = filming
    
    def film(self):
        if self.filming is True:
            print(f'{self.name} ja esta filmando!')
            return #Guard close --> Evitar que o resto da funcao seja executada sem necessidade
        
        print(f'{self.name} esta filmando...')
        self.filming = True #Quando chamarmos o metodo no objeto, o atributo filming se torna True
    
    def photo(self):
        if self.filming is True:
            print(f'{self.name} nao pode fotografar filmando!')
            return
        
        print(f'{self.name} está fotografando!')
    
    def stop_filming(self):
        if self.filming is False:
            print(f'{self.name} nao esta filmando!')
            return
        
        print(f'{self.name} esta parando de filmar...')
        self.filming = False

c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.film() #O atributo filming vira True
c1.film() #Como filming is True, pq ja chamamos o metodo acima, vai retornar o print do if self.filming is True
c1.photo() #c1 nao vai poder fotografar pq filming is True
c1.stop_filming() #Desligando a filmagem da c1 (c1.filming --> False)
c1.photo() #Agora c1 pode fotografar pq nao esta filmando mais
print()
c2.film() #O atributo filming vira True
c2.film() #Como filming is True, pq ja chamamos o metodo acima, vai retornar o print do if self.filming is True
c2.photo() #c2 nao vai poder fotografar pq filming is True
c2.stop_filming() #Desligando a filmagem da c2 (c2.filming --> False)
c2.photo() #Agora c2 pode fotografar pq nao esta filmando mais