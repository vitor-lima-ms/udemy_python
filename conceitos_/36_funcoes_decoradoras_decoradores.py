#Decorator tambem e um padrao de projetos em softwares orientados a objetos
#Decorar --> Adicionar, remover, restringir ou alterar o resultado de uma funcao
#Funcoes decoradoras --> Funcoes que decoram e criam (dentro do seu escopo, tem outra funcao) outras funcoes --> Usar o closure

'''def criar_funcao(funcao): #Funcao decoradora

    def interna(*args, **kwargs):
        print('Vou te decorar.')
        for arg in args:
            is_string(arg)
        #Poderiamos modificar o resultado aqui (antes)
        resultado = funcao(*args, **kwargs)
        #Poderiamos modificar o resultado aqui (depois)
        print('Ok, agora você foi decorada.')
        return resultado

    return interna

def inverte_string(string):
    return string[::-1]

def is_string(arg):
    
    if not isinstance(arg, str):
        raise TypeError('Deve ser string!')



inverte_string_checando_parametro = criar_funcao(inverte_string) #Me retorna a funcao interna
invertida = inverte_string_checando_parametro(123) #Funcao interna recebendo parametros e fazendo a checagem, enviando para a funcao is_string
print(invertida)'''

#Decoradores --> Sao usados para fazer o Python usar as funcoes decoradoras em outras funcoes
#Sao Syntax Sugar --> Python tem um recurso que facilita o uso dos decoradores sem ter que escrever um codigo tao longo quanto o apresentado acima

'''def criar_funcao(funcao): #Funcao decoradora

    def interna(*args, **kwargs):
        print('Vou te decorar.')
        for arg in args:
            is_string(arg)
        
        resultado = funcao(*args, **kwargs)
        print('Ok, agora você foi decorada.')
        return resultado

    return interna

@criar_funcao #Decorador --> Faz tudo que a gente fez acima na funcao inverte_string --> Passa automaticamente a inverte_string para a criar_funcao
def inverte_string(string):
    return string[::-1]

def is_string(arg):
    
    if not isinstance(arg, str):
        raise TypeError('Deve ser string!')


invertida = inverte_string('Vitor')
print(invertida)'''

#Decoradores com parametros
def decorator_param(order): #Para pegar os parametros do decorador

    def decorator(func): #Para pegar a funcao a ser decorada
        print('Decorator', order)

        def new_my_sum(*args, **kwargs): #Funcao que de fato sera executada

            result = func(*args, **kwargs)
            final = f'{result} {order}'
            return final
        
        return new_my_sum
    
    return decorator

@decorator_param(order='3')
@decorator_param(order='2')
@decorator_param(order='1') #Ordem de execucao
def my_sum(x, y):
    return x + y

ten_plus_five = my_sum(10, 5)
print(ten_plus_five)