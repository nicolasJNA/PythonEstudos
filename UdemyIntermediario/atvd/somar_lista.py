def somaLista(l1,l2):
    max_indice = min(len(l1),len(l2))
    return [
        l1[i]+l2[i] for i in range(max_indice)
    ]

lista1 = [2,3,6,98,54]
lista2 = [6,5,8,32]

print(somaLista(lista1,lista2))