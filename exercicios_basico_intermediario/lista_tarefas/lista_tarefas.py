import estilizacao, listar, desfazer, refazer
import json

try:
    with open(
    '/home/vitor/udemy_python/exercicios/lista_tarefas/lista_tarefas.json',
    'r',
    ) as file:
        todo_list = json.load(
            file

    )
except FileNotFoundError:
    todo_list = []
    with open(
    '/home/vitor/udemy_python/exercicios/lista_tarefas/lista_tarefas.json',
    'x'
    ) as file:
      json.dump(
          todo_list,
          file,
          ensure_ascii=False
      ) 

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
        with open(
            '/home/vitor/udemy_python/exercicios/lista_tarefas/lista_tarefas.json',
            'w',
            ) as file:
            json.dump(
                todo_list,
                file,
                indent=2,
                ensure_ascii=False
            )
        break
    
    else:
        todo_list.append(opt)
        estilizacao.header()
        listar.listar(todo_list)