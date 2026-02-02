# filtro: uso do if no final da lista compahision

import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
lista = [
    {'nome':'pato', 'preco':50},
    {'nome':'galinha','preco':25},
    {'nome':'peixe','preco':10},
]

lista_nova = [
    {'nome':elementos['nome'], 'preco': elementos['preco']*1.05}   
    if elementos['preco'] > 20 else {**elementos}
    for elementos in lista
    if elementos['preco'] < 20
]

p(lista_nova)

# # uso de filtro if
# lista = [n for n in range(10) if n < 5]
# print(lista)