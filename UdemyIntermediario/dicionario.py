# chave valor 

pessoa = {
    'nome':'Nicolas',
    'sobrenome':'Justo',
    'altura': '1,75',
    'endereços': [{'pais':'Brasil', 'cidade':'recife'},
                  {'pais': 'Mexico', 'cidade':'novo Mexico'}]
    }

#print(pessoa, type(pessoa))
print(pessoa['endereços'][1]['pais'])