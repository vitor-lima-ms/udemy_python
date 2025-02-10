#csv.reader --> Le o csv em formato de lista
#csv.DictReader --> Le o csv em formato de dicionario
from pathlib import Path
import csv

file_path = Path(__file__).parent.absolute() / '08_csv.csv'

'''with open(file_path, 'r') as file: #Retorna lista
    reader = csv.reader(file)
    #next(reader) #Podemos utilizar esse artificio para pular a linha com cabecalhos

    for line in reader:
        print(line) #Como e uma lista, podemos utilizar os metodos de lista'''

'''with open(file_path, 'r') as file: #Retorna dict
    dict_reader = csv.DictReader(file)
    #next(reader) #Podemos utilizar esse artificio para pular a linha com cabecalhos

    for line in dict_reader:
        print(line)) #Como e uma lista, podemos utilizar os metodos de lista'''

#csv.writer
#csv.DictWriter

family_list = [
{'nome': 'Vitor', 'idade': 24},
{'nome': 'Geraldo', 'idade': 64},
{'nome': 'Débora', 'idade': 33},
{'nome': 'Simone', 'idade': 55},
]

column_names_csv = family_list[0].keys()

'''with open(file_path, 'w') as file: #Funciona com uma lista de listas tb --> So tirar o values
    writer = csv.writer(file)

    writer.writerow(column_names_csv)

    for client in family_list:
        writer.writerow(client.values())'''

with open(file_path, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=column_names_csv)

    writer.writeheader() #Escreve o que e passado no fieldnames

    for client in family_list:
        writer.writerow(client)