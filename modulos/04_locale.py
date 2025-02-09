#Traduz os termos, muda a forma como os numeros aparecem (separador decimal), muda a forma de exibicao das datas

import locale #Sempre settar no arquivo __main__
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') #Podemos mudar tudo ou coisas especificas como TIME, MONETARY, NUMERIC etc. --> Podemos settar um locale e uma codificacao de caractere mas o sistema operacional precisa ter suporte a ele --> Para ver os locais suportados pelo sistema (Linux) --> locale -a no terminal

print(calendar.month(2025, 5))

print(locale.getlocale()) #Retorna o locale do sistema e a codificacao de caractere