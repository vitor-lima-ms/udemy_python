#JSON --> JavaScript Object Notation --> Todas as linguagens praticamente aceitam o formato JSON
#E uma estrutura de dados que permite a serializacao de objetos em textos simples, facilitando a transmissao de dados atraves da rede, APIs web, entre outros --> Funcoes e classes nao sao suportados
#O JSON suporta os seguintes tipos de dados:
    #Numeros --> Inteiros e com ponto flutuante
    #Strings --> Envolvidas por aspas duplas
    #Bool --> true e false (com letra minuscula mesmo)
    #Arrays --> Listas 
    #Objetos --> Conjuntos de pares chave/valor (analogo ao dicionario em Python) --> No JSON, apenas strings podem ser chave
    #null --> Valor que representa ausencia de valor
#Ao converter de Python para JSON
    #dict --> object
    #list, tuple --> array
    #str --> string
    #int, float --> number
    #True, False --> true, false
    #None --> null
    #Converter de JSON para Python retorna o caminho inverso

#json.dumps e json.loads --> s no final e de string --> So aceitam e retornam strings

"""import json
from pprint import pprint #print mais bonitin
from typing import TypedDict #Para tipar as chaves do JSON e facilitar a importacao para o Python

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    caracters: list[str]
    budget: None | float

str_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "caracters": ["Frodo", "Sam", "Gandalf"],
    "budget": null
}
'''
movie: Movie = json.loads(str_json)

json_dump = json.dumps(movie, ensure_ascii=False, indent=2) """

#json.dump e json.load --> Sem o s no final --> Trabalhar com arquivos

import json
import os
from typing import TypedDict

FILE_NAME = '/06_json.json'
ABS_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__) + FILE_NAME))
print(ABS_FILE_PATH)

str_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "caracters": ["Frodo", "Sam", "Gandalf"],
    "budget": null
}
'''

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    caracters: list[str]
    budget: None | float

movie_dict: Movie = json.loads(str_json)

with open(ABS_FILE_PATH, 'w') as file:
    json.dump(movie_dict, file, ensure_ascii=False, indent=2)

with open(ABS_FILE_PATH, 'r') as file:
    movie_dict_load = json.load(file)

print(movie_dict_load)