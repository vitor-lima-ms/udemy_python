#O random gera numeros pseudoaleatorios --> Este modulo nao deve ser usado para seguranca ou uso criptografico --> Motivo: Quanto temos uma mesma entrada e um mesmo algoritmo, a saida pode ser previsivel
#Funcoes
    #seed --> Inicializa o gerador de random --> Utiliza time.time() para gerar o seed
    #random.randrange(inicio, fim, passo) --> Gera um numero inteiro aleatorio dentro de um intervalo especificado
import random
'''r_random = random.randrange(10, 20)
print(r_random)
r_random = random.randrange(10, 20, 2)
print(r_random)'''
    #random.randint(inicio, fim) --> Gera um numero inteiro aleatorio dentro de um intervalo especificado sem passo
'''r_int = random.randint(0, 100)
print(r_int)'''
    #random.uniform(inicio, fim) --> Gera um numero flutuante aleatorio dentro de um intarvalo
'''r_unf = random.uniform(0, 100)
print(r_unf)'''
    #random.shuffle(SequenciaMutavel) --> Embaralha a lista original --> Podemos fazer um deepcopy antes
my_list = [n for n in range(0, 101)]
'''random.shuffle(my_list)
print(my_list)'''
    #random.choice(iteravel) --> Escolhe um elemento do iteravel
'''r_chc = random.choice(my_list)
print(r_chc)'''
    #random.choices(iteravel, k=N) --> Escolhe elementos do iteravel e retorna outro iteravel (repete)
r_chcs = random.choices(my_list, k=10)
print(r_chcs)
    #random.sample(iteravel, k=N) --> Escolhe elementos do iteravel e retorna outro iteravel (nao repete)
'''my_new_list = random.sample(my_list, 10)
print(my_new_list)'''