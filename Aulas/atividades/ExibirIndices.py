#exiba os indices da lista

lista = ['maria','nicolas','jose','helena','alguisto']
indices = 0
for contagem in lista:
    print(f'{indices}-{contagem}')
    indices += 1

indices = range(len(lista))
for indice in indices:
    print(lista[indice])