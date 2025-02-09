#Maria pegou um emprestimo de R$1.000.000, que devera ser pago em 5 anos. A data que ela pegou o emprestimo foi 20/12/2020 e o vencimento de cada parcela e no dia 20 de cada mes
#Objetivo:
    #Criar a data do emprestimo
    #Criar a data do final do emprestimo
    #Mostrar todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

VALOR_TOTAL = 1E6

start_date = datetime.strptime('20/01/2021', '%d/%m/%Y')
end_date = start_date + relativedelta(years=5)

installments_number = relativedelta(end_date, start_date).years * 12
installments_value = round(VALOR_TOTAL / installments_number, 2)

for installment in range(1, installments_number + 1):
    print(f'{installment}a parcela.')
    if installment == 1:
        installment_due_date = start_date
        fmt_installment_due_date = installment_due_date.strftime('%d/%m/%Y')
        print(f'{fmt_installment_due_date}\tR$ {installments_value:,}\n')
        continue

    installment_due_date += relativedelta(months=1)
    fmt_installment_due_date = installment_due_date.strftime('%d/%m/%Y')
    print(f'{fmt_installment_due_date}\tR$ {installments_value:,}\n')