import desfazer

def refazer(usr_list):
    if len(desfazer.regret_tasks) == 0:
        return print('Nada a refazer!!!'.upper())

    usr_list.append(desfazer.regret_tasks[0])
    desfazer.regret_tasks.pop(0)
    return usr_list