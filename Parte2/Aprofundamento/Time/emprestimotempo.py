from dateutil.relativedelta import relativedelta
from datetime import datetime

valor_total = 1_000_000
data_emprestimo = datetime(2000,1,1)
data_anos = relativedelta(years=5)
data_final = data_emprestimo + data_anos

parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    parcelas.append(data_parcela)
    data_parcela += relativedelta(month=+1)

for data in data_parcela:
    print(data)
