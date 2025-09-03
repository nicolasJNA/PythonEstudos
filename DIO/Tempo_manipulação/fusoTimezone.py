"""
Corrigindo fusos horarios
"""
from datetime import datetime,timedelta,timezone

data_saoPaulo = datetime.now(timezone(timedelta(hours=-3)))
data_oslo = datetime.now(timezone(timedelta(hours=2)))

print(data_oslo)
print(data_saoPaulo)