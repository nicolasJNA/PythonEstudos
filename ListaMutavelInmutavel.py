"""
Diferneça entre os dados mutaveis 
    copiando o valor (imutavel)
    aponta pro mesmo valor
"""

lista_a =[4,5,'oi',True, None]
lista_b = lista_a.copy()

lista_a[0] = 10
print(lista_b)