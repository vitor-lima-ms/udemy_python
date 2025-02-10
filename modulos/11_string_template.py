#Utilizada para substituir variaveis em texto
#Metodos
    #substitute --> Substitui mas gera erros se faltar chaves
    #safe_substitute --> Substitui sem gerar erros
#Podemos trocar o delimitador e outras coisas criando uma subclasse de template

import locale
from datetime import datetime
from pprint import pprint
import string
from pathlib import Path

PATH_FILE = Path(__file__).parent / '11_string_template.txt'

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def brl_conversion(num: float) -> str:
    brl = 'R$ ' + locale.currency(val=num, symbol=False, grouping=True) #Conversao monetaria --> Tem que dar o setlocale antes --> symbol=False para ele nao colocar o simbolo --> grouping=True para delimitar milhares, milhoes etc.
    return brl

date = datetime.now()
data = dict(
    name='Vitor',
    value=brl_conversion(1_234_567),
    date = date.strftime('%d/%m/%Y'),
    company='V. L.',
    phone_number = '+55 (31) 9 1234-5678'
)

text = '''
Prezado(a) $name,

Informamos que sua mensalidade será cobrada no valor de $value no dia $date. Caso deseje cancelar o serviço, entre em contato com a $company pelo telefone $phone_number.

Atenciosamente,

${company},

Abraços
'''

'''print(template.substitute(data))
print(template.safe_substitute(data)) #N da erro se n tivermos alguma variavel'''

with open(PATH_FILE, 'r') as file:
    text = file.read()
    template = string.Template(text)
    print(template.safe_substitute(data))

class MyTemplate(string.Template): #Permite que utilizemos um delimitador diferente do $
    delimiter = '%'