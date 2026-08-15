from datetime import datetime, timedelta

fmt = '%d-%m-%Y %H:%M:%S'

data_inicio = datetime.strptime('10-02-1999 12:43:00',fmt)
data_fim = datetime.strptime('12-10-2000 00:43:50',fmt)

delta = timedelta(days=10)
print(data_inicio + delta)

print(data_fim > data_inicio)