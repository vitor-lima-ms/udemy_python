nome = 'Vitor'

iterador = iter(nome) #Objeto iterador

while True:
    
    try:
        
        print(next(iterador)) #Solicita ao objeto iterador o proximo elemento do objeto iteravel
    
    except StopIteration: #Tratando um erro especifico

        break

#E exatamente isso que o for faz