regret_tasks = []

def desfazer(usr_list):
    if len(usr_list) == 0:
        return print('Nada a desfazer!!!'.upper())

    last_item = usr_list.pop()
    regret_tasks.insert(0, last_item)
    return usr_list