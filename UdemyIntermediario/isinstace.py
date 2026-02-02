# isinstace - metodo para saber se um ubjeto é de determinado tipo
lista = [
    'a',1,1.1,'true', False, [1,2,3],
    (4,9),{0,1},{'valor':10},
]

for item in lista:
    if isinstance(item,set):
        item.add(5)
        print(item, isinstance(item,set))
    
    if isinstance(item,str):
        item.upper()
        print(item.upper(),isinstance(item,set))