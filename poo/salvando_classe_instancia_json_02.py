import json
from salvando_classe_instancia_json_01 import BrazilianPerson

def open_instance(file):
    with open(f'{file}.json', 'r') as file:
        list_dict_instance = json.load(file)
        return list_dict_instance

brazilian_people_list = open_instance('brazilian_people')

p1 = BrazilianPerson(**brazilian_people_list[0])
p2 = BrazilianPerson(**brazilian_people_list[1])

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)