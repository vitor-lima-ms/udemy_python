contador = 0

while True:

    contador += 1

    if contador == 1:
        
        num1_str = input('Digite um número: ')
        
        while (num1_str.replace('.', '').replace(',', '').isnumeric() is False):
            
            print('Isso não é um número!')

            num1_str = input('Digite um número: ')
    
    elif contador == 2:

        num2_str = input('Digite outro número: ')
        
        while (num2_str.replace('.', '').replace(',', '').isnumeric() is False):
            
            print('Isso não é um número!')

            num2_str = input('Digite outro número: ')
    
    elif contador == 3:

        operador = input('Digite um operador [+, -, * ou /]: ')

        while operador not in '+-*/':

            print('Esse não é um operador válido!')

            operador = input('Digite um operador [+, -, * ou /]: ')
    
    elif contador == 4:

        if operador == '+':
    
            resultado = float(num1_str) + float(num2_str)

            print(f'O resultado da operação é: {resultado}!')

        elif operador == '-':

            resultado = float(num1_str) - float(num2_str)

            print(f'O resultado da operação é: {resultado}!')

        elif operador == '*':

            resultado = float(num1_str) * float(num2_str)
            
            print(f'O resultado da operação é: {resultado}!')

        else:

            resultado = float(num1_str) / float (num2_str)

            print(f'O resultado da operação é: {resultado}!')

        continuar = input('Deseja realizar mais alguma operação [S/N]? ')

        while (continuar not in 'Nn') and (continuar not in 'Ss'):

            print('Opção inválida!')

            continuar = input('Deseja realizar mais alguma operação [S/N]? ')
        
        if continuar in 'Nn':

            break

        else:

            contador = 0

print('Volte sempre!')