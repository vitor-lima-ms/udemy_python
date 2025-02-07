import estilizacao, listar, desfazer, refazer

todo_list = []

while True:

    print('Comandos: listar, desfazer, refazer ou sair.')
    opt = input('Digite uma tarefa ou comando: ').lower()

    while opt.replace(' ', '').isnumeric() is True or opt.replace(' ', '').isalpha() is False:
        print('Opção inválida!')
        opt = input('Digite uma tarefa ou comando: ').lower()
    
    if opt == 'listar':
        estilizacao.header()
        listar.listar(todo_list)

    
    elif opt == 'desfazer':
        desfazer.desfazer(todo_list)
        estilizacao.header()
        listar.listar(todo_list)
    
    elif opt == 'refazer':
        refazer.refazer(todo_list)
        estilizacao.header()
        listar.listar(todo_list)

    
    elif opt == 'sair':
        break
    
    else:
        todo_list.append(opt)
        estilizacao.header()
        listar.listar(todo_list)