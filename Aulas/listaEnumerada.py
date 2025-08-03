lista = ['maria', 'joao','jose']
lista.append('pedro')

#lista_enumerada = enumerate(lista)

for item in enumerate(lista):
    indice,nome = item
    print(indice,nome)

"""
O enumerate enumera cada item da lista, o python n tem a
facilidade para imprimir o Index da lista. logo faz-se nescessario
usar enumerate()
"""
