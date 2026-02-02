lista = [
    {'nome':'pato', 'preco':50},
    {'nome':'galinha','preco':25},
    {'nome':'peixe','preco':10},
]

lista_nova = [
    {'nome':elementos['nome'], 'preco': elementos['preco']*1.05}   
    if elementos['preco'] > 20 else {**elementos}
    for elementos in lista
]
print(*lista_nova, sep='\n')