#Funcoes que podem ser chamar de volta --> Loop
#Uteis para dividir problemas grandes em partes menores
#Toda funcao recursiva deve ter:
    #Um problema que possa ser dividido em partes menores
    #Um caso recursivo que resolve o pequeno problema
    #Um caso base que para a recursao

'''def recursive(start=0, end=3):
    #Caso recursivo --> Contar ate 10
    #print(start, end) #So pra entender a logica
    start += 1
    if start == end:
        return end
    return recursive(start)

print(recursive())'''

#Fatorial

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))