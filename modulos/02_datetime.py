#Criando datas com o modulo datetime
    #datetime(ano, mes, dia)
    #datetime(ano, mes, dia, horas, minutos, segundos)
    #datetime.strptime('data', 'formato')
    #datetime.now()
#Para timezones --> pip install pytz types-pytz

'''from datetime import datetime

date00 = datetime(2024, 2, 9) #Apenas numeros inteiros
print(date00)

date01 = datetime(2024, 2, 9, 12, 30, 30) #Hora, minutos e segundos sao opcionais
print(date01)

date02 = datetime.strptime('2024-02-09', '%Y-%m-%d') #Criar data a partir de string --> O datetime.strftime é para formatar strings como data --> Se minha data estivesse com /, e so substituir os - por /
print(date02)'''

#Obtendo a data atual e timezones

'''from datetime import datetime
from pytz import timezone
#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones --> Lista de todas as timezones --> ctrl +f para achar mais facil

date00 = datetime.now(timezone('Asia/Tokyo')) #Podemos passar um timezone especifico dentro dos ()
print(date00)

date01 = datetime(2024, 2, 9, 12, 30, 30, tzinfo=timezone('Asia/Tokyo')) #A data criada vai ser precisa para a timezone especificada
print(date01)

date02 = datetime.now().timestamp() #Unix Timestamp --> Contagem de segundos de 01/01/1970 ate agora --> Muito utilizado na programacao
print(date02)

date03 = datetime.fromtimestamp(1739116154.322864) #Podemos criar uma data a partir do Unix Timestamp
print(date03)'''

#Comparando datas


#Formatando datas

'''from datetime import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('17/05/2000 00:00:00',fmt)
end_date = datetime.strptime('09/02/2025 13:30:00',fmt)

print(start_date > end_date)
print(start_date < end_date)
print(start_date == end_date)

time_delta = end_date - start_date
print(time_delta.days, time_delta.seconds, time_delta.microseconds) #Retorna o que e chamado de timedelta
print(time_delta.total_seconds()) #Diferenca total em segundos

my_delta = timedelta(days=10) #Podemos somar/subtrair o timedelta de uma data
print(end_date + my_delta)
print(end_date - my_delta)

print(end_date + relativedelta(day=10, month=5, years=2)) #Modulo dateutil --> Estamos criando um delta relativo a data que estamos trabalhando
print(relativedelta(end_date, start_date)) #Retorna um objeto bem detalhado quanto a diferenca entre as duas datas informadas'''

#Formatando datas --> strftime ao inves de strptime --> Ja temos a data

'''from datetime import datetime

date = datetime.now()
print(date)
fmt = '%d/%m/%Y'
fmt_date = date.strftime(fmt) #Agora passamos o objeto antes do . --> Retorna uma string
print(fmt_date)'''

#Obtendo dia, mes e ano de forma facil

from datetime import datetime

date = datetime.now()
print(date.day) #Todos retornam um int
print(date.month)
print(date.year)