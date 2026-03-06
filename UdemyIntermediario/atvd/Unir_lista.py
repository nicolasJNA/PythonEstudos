from itertools import zip_longest

def zipper(a,b):
    final = []
    cont = 0
    if(len(a)<len(b)):
        menor = len(a) - 1
    else:
        menor = len(b) - 1
    while(True):
        final.append((a[cont],b[cont]))
        if(not cont< menor):
            break
        cont += 1
    return final

#Aprimorado
def zip(lista1,lista2):
    indice_max = min(len(lista1),len(lista2))
    return [(lista1[i],lista2[i]) for i in range(indice_max)]

lista1 = ['Salvador','Ubatuba','Belo Horizonte']
lista2 = ['BA','SP','MG','RJ']

print(zipper(lista1,lista2))
print(zip(lista1,lista2))
print(list(zip_longest(lista1,lista2,fillvalue = "Sem cidade")))