"""
Listas em python são mutaveis 
suporta varios valores e tipos
metodos uteis:
    append - insere no ultimo indice
    insert(indice, valor)
    pop- remove o ultimo indice
    del - remove de um indice espec
    clear - limpa a lista
    extend - junta a lista estendendo
Create Read Update Delete
criar  ler  alterar apagar = lista[i] (CRUD)
"""
import os
os.system('clear')

lista = [10,20,30,40]
lista2 = [1,11,13,17]
numero = lista[2]
print(lista)

lista[1] = 5
del lista[3]
lista.append(15)
lista.append(89)
lista.append(100)
ultimo_valor = lista.pop()
print(ultimo_valor)
print(lista)

lista.insert(0,'nicolas')
print(lista)
lista.extend(lista2)
print(lista)