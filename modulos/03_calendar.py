#Usado para coisas genericas de calendarios e datas
#Podemos saber coisas como:
    #Qual o ultimo dia do mes (monthrange)
    #Qual o nome e numero do dia de determinada data (weekday)
    #Criar um calendario em si (monthcalendar)
#Por padrao, os dias da semana sao numerados de 0 (segunda) ate 6 (domingo)

import calendar

#print(calendar.calendar(2025)) #Calendario do ano de 2025
#print(calendar.month(2025, 5))
#print(calendar.monthrange(2025, 5)) #Tupla onde [0] e o numero correspondente do dia da semana do primeiro dia do mes e [1] e q quantidade de dias
#print(list(calendar.day_name)) #Lista com os dias da semana --> Por isso segunda e 0 e domingo 6
#print(calendar.weekday(2025, 5, 31)) #Para saber qual dia da semana corresponde ao ultimo dia do mes de maio nesse caso, mas pode ser utilizado para outros meses --> Basta utilizar o monthrange pra saber se o mes vai ate 28, 29, 30 ou 31
#print(calendar.monthcalendar(2025, 5)) #Uma lista com sublistas onde cada uma representa uma semana, onde cada elemento destas representa o valor do dia do mes --> Se aparecer 0, é pq tal dia da semana nao pertence ao mes em questao --> A ordem como ja visto, e de segunda (0) ate domingo (6)