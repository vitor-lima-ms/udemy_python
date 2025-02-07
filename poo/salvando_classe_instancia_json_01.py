import json

class BrazilianPerson:
    NATIONALITY = 'Brasileiro'
    BIRTH_CONTINENT = 'America do Sul'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def save_instance(any_list):
    with open(f'brazilian_people.json', 'w') as file:
        json.dump(
            any_list,
            file,
            indent=2
        )

p1 = BrazilianPerson('Vitor', 24)
p2 = BrazilianPerson('Maria', 22)

brazilian_people_list = [vars(p1), vars(p2)]

save_instance(brazilian_people_list)