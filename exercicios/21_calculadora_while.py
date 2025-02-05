while True:
        
    num1_str = input('Digite um número: ')
        
    while (num1_str.replace('.', '').replace(',', '').isnumeric() is False):
            
        print('Isso não é um número!')

        num1_str = input('Digite um número: ')
    
    num2_str = input('Digite outro número: ')
        
    while (num2_str.replace('.', '').replace(',', '').isnumeric() is False):
            
        print('Isso não é um número!')

        num2_str = input('Digite outro número: ')
    
    operador = input('Digite um operador [+, -, * ou /]: ')

    while (operador not in '+-*/') or (len(operador) > 1):

        print('Esse não é um operador válido!')

        operador = input('Digite um operador [+, -, * ou /]: ')
    
    if operador == '+':
    
        resultado = float(num1_str.replace(',', '.')) + float(num2_str.replace(',', '.'))

        print(f'O resultado da operação é: {resultado}!')

    elif operador == '-':

        resultado = float(num1_str.replace(',', '.')) - float(num2_str.replace(',', '.'))

        print(f'O resultado da operação é: {resultado}!')

    elif operador == '*':

        resultado = float(num1_str.replace(',', '.')) * float(num2_str.replace(',', '.'))
            
        print(f'O resultado da operação é: {resultado}!')

    else:

        resultado = float(num1_str.replace(',', '.')) / float (num2_str.replace(',', '.'))

        print(f'O resultado da operação é: {resultado:.2f}!')

    continuar = input('Deseja realizar mais alguma operação [S/N]? ')

    while (continuar not in 'Nn') and (continuar not in 'Ss'):

        print('Opção inválida!')

        continuar = input('Deseja realizar mais alguma operação [S/N]? ')
        
    if continuar in 'Nn':

        break

print('Volte sempre!')