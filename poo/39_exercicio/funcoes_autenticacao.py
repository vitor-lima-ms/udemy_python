def client_auth(bank: object, client: object) -> bool:
    for bank_client in bank.__dict__['clients']:
        
        if bank_client == client.__dict__['_name']:
            print('Cliente encontrado.')
            return True
    
    return False

def ag_auth(bank: object, client: object) -> bool:
    found_client_index = bank.__dict__['clients'].index(client.name)

    if bank.__dict__['ags'][found_client_index] ==\
    client.acc_.__dict__['ag']:
        print('Agência encontrada.')
        return True
    
    return False

def acc_auth(bank: object, client: object) -> bool:
    found_client_index = bank.__dict__['clients'].index(client.name)
    
    if bank.__dict__['acc_numbers'][found_client_index] ==\
    client.acc_.__dict__['acc_number']:
        print('Conta encontrada. Autorizando saque...')
        return True
    
    return False