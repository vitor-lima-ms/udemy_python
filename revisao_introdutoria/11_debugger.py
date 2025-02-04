#Devemos criar o arquivo .json para funcionar corretamente --> So clicar no botao de debug do VS Code
#Devemos marcar um breakpoint --> Bolinha vermelha do lado esq do numero da linha

a = 1
if a == 1:
    print('a = 1')
elif a == 2: #O interpretador nao confere a condicao por ser elif
    print('a = 2')
if a == 2: #O interpretador confere a condicao por ser if, mesmo que o if a == 1 seja verdadeiro
    print('a = 2')