"""
transformando strings em tipos datetime e vise versa
e manipulando o formato do datetime
"""
import datetime

data = datetime.datetime.now()
nova_data = data.strftime('%d/%m/%Y %H:%m %p') 
print(nova_data)

str_data = '10/02/2004 17:45:32'
print(type(str_data))
print(str_data)

# Formato corrigido para corresponder à str_data
nova_str_data = datetime.datetime.strptime(str_data, "%d/%m/%Y %H:%M:%S")

print(type(nova_str_data))
print(nova_str_data)